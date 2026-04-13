"""
Tests for the ASPICE Capability Checker.
Run with:  python -m pytest tests/ -v
"""

from __future__ import annotations

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.aspice_knowledge import (
    ASSESSMENT_QUESTIONS,
    CAPABILITY_LEVELS,
    LEVEL_ACHIEVEMENT_RULES,
    PROCESS_GROUPS,
    RATING_SCALE,
)
from src.rag_engine import AspiceAgent, assess_capability_level


# ---------------------------------------------------------------------------
# Knowledge base tests
# ---------------------------------------------------------------------------


class TestAspiceKnowledge:
    def test_capability_levels_count(self):
        assert len(CAPABILITY_LEVELS) == 6  # Levels 0-5

    def test_all_levels_have_name(self):
        for level, data in CAPABILITY_LEVELS.items():
            assert "name" in data, f"Level {level} missing 'name'"

    def test_rating_scale_keys(self):
        assert set(RATING_SCALE.keys()) == {"N", "P", "L", "F"}

    def test_rating_scores_ascending(self):
        scores = [RATING_SCALE[k]["score"] for k in ("N", "P", "L", "F")]
        assert scores == sorted(scores)

    def test_process_groups_present(self):
        for expected in ("SWE", "SYS", "MAN", "SUP", "ACQ"):
            assert expected in PROCESS_GROUPS

    def test_swe_processes_complete(self):
        swe = PROCESS_GROUPS["SWE"]["processes"]
        for proc_id in ("SWE.1", "SWE.2", "SWE.3", "SWE.4", "SWE.5", "SWE.6"):
            assert proc_id in swe, f"{proc_id} not found in SWE processes"

    def test_each_process_has_required_fields(self):
        for group in PROCESS_GROUPS.values():
            for proc_id, proc in group["processes"].items():
                for field in ("name", "purpose", "outcomes", "work_products", "base_practices"):
                    assert field in proc, f"{proc_id} missing '{field}'"
                assert len(proc["outcomes"]) >= 1
                assert len(proc["base_practices"]) >= 1

    def test_assessment_questions_for_all_pas(self):
        expected_pas = {"PA 1.1", "PA 2.1", "PA 2.2", "PA 3.1", "PA 3.2", "PA 4.1", "PA 4.2", "PA 5.1", "PA 5.2"}
        for pa in expected_pas:
            assert pa in ASSESSMENT_QUESTIONS, f"No assessment questions for {pa}"
            assert len(ASSESSMENT_QUESTIONS[pa]) >= 3

    def test_level_achievement_rules_defined(self):
        for level in range(1, 6):
            assert level in LEVEL_ACHIEVEMENT_RULES


# ---------------------------------------------------------------------------
# Capability level assessment logic tests
# ---------------------------------------------------------------------------


class TestCapabilityLevelAssessment:
    def test_all_not_achieved_gives_level_0(self):
        ratings = {pa: "N" for pa in ("PA 1.1", "PA 2.1", "PA 2.2")}
        result = assess_capability_level(ratings)
        assert result["achieved_level"] == 0

    def test_pa11_fully_gives_level_1(self):
        result = assess_capability_level({"PA 1.1": "F"})
        assert result["achieved_level"] == 1

    def test_pa11_largely_does_not_give_level_1(self):
        result = assess_capability_level({"PA 1.1": "L"})
        assert result["achieved_level"] == 0

    def test_level_2_requires_pa11_fl_and_pa21_pa22_f(self):
        ratings = {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"}
        result = assess_capability_level(ratings)
        assert result["achieved_level"] == 2

    def test_level_2_fails_if_pa21_is_l(self):
        ratings = {"PA 1.1": "F", "PA 2.1": "L", "PA 2.2": "F"}
        result = assess_capability_level(ratings)
        assert result["achieved_level"] < 2

    def test_level_3_full_ratings(self):
        ratings = {
            "PA 1.1": "F",
            "PA 2.1": "L",
            "PA 2.2": "L",
            "PA 3.1": "F",
            "PA 3.2": "F",
        }
        result = assess_capability_level(ratings)
        assert result["achieved_level"] == 3

    def test_result_has_required_keys(self):
        result = assess_capability_level({"PA 1.1": "F"})
        for key in ("achieved_level", "level_name", "level_description", "gaps", "recommendations", "pa_details"):
            assert key in result

    def test_gaps_populated_when_below_target(self):
        result = assess_capability_level({"PA 1.1": "N"})
        assert len(result["gaps"]) > 0

    def test_case_insensitive_input(self):
        result = assess_capability_level({"pa 1.1": "f"})
        assert result["achieved_level"] == 1

    def test_missing_pa_defaults_to_n(self):
        result = assess_capability_level({})
        assert result["achieved_level"] == 0


# ---------------------------------------------------------------------------
# AspiceAgent tests
# ---------------------------------------------------------------------------


class TestAspiceAgent:
    @pytest.fixture(scope="module")
    def agent(self):
        a = AspiceAgent()
        a.build_knowledge_base()
        return a

    def test_build_knowledge_base(self, agent):
        assert agent._built

    def test_get_all_processes_returns_list(self, agent):
        procs = agent.get_all_processes()
        assert isinstance(procs, list)
        assert len(procs) >= 10

    def test_get_process_info_swe1(self, agent):
        info = agent.get_process_info("SWE.1")
        assert info["name"] == "Software Requirements Analysis"
        assert "purpose" in info

    def test_get_process_info_unknown(self, agent):
        info = agent.get_process_info("UNKNOWN.99")
        assert info == {}

    def test_get_capability_level_info(self, agent):
        info = agent.get_capability_level_info(2)
        assert info["name"] == "Managed"

    def test_get_assessment_questions(self, agent):
        qs = agent.get_assessment_questions("PA 2.1")
        assert len(qs) >= 5

    def test_assess_process_returns_structured_result(self, agent):
        result = agent.assess_process("SWE.1", {"PA 1.1": "F"})
        assert "achieved_level" in result
        assert result["process_id"] == "SWE.1"

    def test_chat_returns_string(self, agent):
        answer = agent.chat("What is capability level 2?")
        assert isinstance(answer, str)
        assert len(answer) > 10

    def test_chat_history_grows(self, agent):
        initial = len(agent.get_history())
        agent.chat("What is PA 3.1?")
        assert len(agent.get_history()) == initial + 2

    def test_clear_history(self, agent):
        agent.clear_history()
        assert agent.get_history() == []

    def test_add_custom_knowledge(self, agent):
        agent.add_custom_knowledge(
            "Custom note: our SWE.1 uses DOORS NG for requirements management.",
            doc_id="TEST_DOC",
        )
        answer = agent.chat("What tool does our organisation use for requirements management?")
        assert isinstance(answer, str)
        assert len(answer) > 10
        # The custom doc should be retrievable — "DOORS" must appear in the context/answer
        assert "DOORS" in answer

    def test_assess_multiple_processes(self, agent):
        assessments = {
            "SWE.1": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"},
            "MAN.3": {"PA 1.1": "F"},
        }
        results = agent.assess_multiple_processes(assessments)
        assert "summary" in results
        assert "results" in results
        assert "SWE.1" in results["results"]
        assert results["summary"]["processes_assessed"] == 2

    def test_improvement_roadmap(self, agent):
        assessments = {"SWE.1": {"PA 1.1": "F", "PA 2.1": "N", "PA 2.2": "N"}}
        roadmap = agent.get_improvement_roadmap(assessments, target_level=3)
        assert roadmap["target_level"] == 3
        assert "SWE.1" in roadmap["processes"]
        plan = roadmap["processes"]["SWE.1"]
        assert plan["status"] in ("achieved", "gap")
