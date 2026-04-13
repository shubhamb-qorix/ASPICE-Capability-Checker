"""
ASPICE Capability Checker — CLI interface
Usage:
    python cli.py chat
    python cli.py assess --process SWE.1
    python cli.py roadmap --target 3 --processes SWE.1 SWE.2 MAN.3
    python cli.py info --process SWE.1
    python cli.py levels
"""

from __future__ import annotations

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))


def _print_banner() -> None:
    print(
        "\n"
        "╔══════════════════════════════════════════════════════╗\n"
        "║         ASPICE Capability Checker  v1.0              ║\n"
        "║    RAG Agent — ASPICE v4.0 / ISO/IEC 33020           ║\n"
        "╚══════════════════════════════════════════════════════╝\n"
    )


def _build_agent():
    from src.rag_engine import AspiceAgent
    agent = AspiceAgent()
    print("⏳ Building ASPICE v4.0 knowledge base…")
    agent.build_knowledge_base()
    print("✅ Knowledge base ready.\n")
    return agent


# ---------------------------------------------------------------------------
# Sub-commands
# ---------------------------------------------------------------------------


def cmd_chat(args: argparse.Namespace) -> None:
    agent = _build_agent()
    print("💬 ASPICE Q&A Chat — type 'quit' to exit\n")
    while True:
        try:
            q = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("quit", "exit", "q"):
            break
        if not q:
            continue
        answer = agent.chat(q)
        print(f"\nAgent:\n{answer}\n")


def cmd_assess(args: argparse.Namespace) -> None:
    agent = _build_agent()
    from src.aspice_knowledge import RATING_SCALE

    print(f"📊 Assessing process: {args.process}\n")
    pa_list = ["PA 1.1", "PA 2.1", "PA 2.2", "PA 3.1", "PA 3.2", "PA 4.1", "PA 4.2", "PA 5.1", "PA 5.2"]
    pa_ratings: dict[str, str] = {}

    if args.ratings:
        # Accept JSON string: '{"PA 1.1": "F", "PA 2.1": "L"}'
        pa_ratings = json.loads(args.ratings)
    else:
        print("Rate each Process Attribute (N / P / L / F):")
        for pa in pa_list:
            while True:
                r = input(f"  {pa}: ").strip().upper()
                if r in RATING_SCALE:
                    pa_ratings[pa] = r
                    break
                print("  ❌ Invalid — enter N, P, L, or F")

    result = agent.assess_process(args.process, pa_ratings)
    print(f"\n{'='*55}")
    print(f"  Process  : {result['process_id']}")
    print(f"  Level    : {result['achieved_level']} — {result['level_name']}")
    print(f"{'='*55}")

    if result["gaps"]:
        print("\n⚠️  Gaps:")
        for g in result["gaps"]:
            print(f"  • {g}")

    if result["recommendations"]:
        print("\n💡 Recommendations:")
        for r in result["recommendations"]:
            print(f"  • {r}")

    print()


def cmd_roadmap(args: argparse.Namespace) -> None:
    agent = _build_agent()
    from src.aspice_knowledge import RATING_SCALE

    print(f"🗺️  Improvement Roadmap — Target Level {args.target}\n")
    current_state: dict[str, dict[str, str]] = {}

    for proc in args.processes:
        print(f"\nRate PAs for {proc} (N/P/L/F):")
        pa_ratings: dict[str, str] = {}
        for pa in ["PA 1.1", "PA 2.1", "PA 2.2", "PA 3.1", "PA 3.2"]:
            while True:
                r = input(f"  {pa}: ").strip().upper()
                if r in RATING_SCALE:
                    pa_ratings[pa] = r
                    break
                print("  ❌ Invalid — enter N, P, L, or F")
        current_state[proc] = pa_ratings

    roadmap = agent.get_improvement_roadmap(current_state, args.target)

    print(f"\n{'='*55}")
    print(f"  Target: Capability Level {roadmap['target_level']}")
    print(f"{'='*55}")
    for proc_id, plan in roadmap["processes"].items():
        if plan["status"] == "achieved":
            print(f"\n  ✅ {proc_id}: Target already achieved (Level {plan['current_level']})")
        else:
            print(
                f"\n  🔧 {proc_id}: Current Level {plan['current_level']} → Target Level {plan['target_level']}"
            )
            for i, action in enumerate(plan["actions"], 1):
                print(f"     {i}. {action}")
    print()


def cmd_levels(args: argparse.Namespace) -> None:
    from src.aspice_knowledge import CAPABILITY_LEVELS

    print("📏 ASPICE v4.0 Capability Levels\n")
    for level, data in CAPABILITY_LEVELS.items():
        print(f"  Level {level}: {data['name']}")
        print(f"    {data['description'][:120]}…")
        for pa in data.get("process_attributes", []):
            print(f"    ├ {pa['id']} — {pa['name']}")
        print()


def cmd_info(args: argparse.Namespace) -> None:
    agent = _build_agent()
    info = agent.get_process_info(args.process)
    if not info:
        print(f"❌ Process '{args.process}' not found.")
        return

    print(f"\n{'='*55}")
    print(f"  {args.process} — {info['name']}")
    print(f"  Group: {info['group']}")
    print(f"{'='*55}")
    print(f"\nPurpose:\n  {info['purpose']}\n")
    print("Outcomes:")
    for o in info["outcomes"]:
        print(f"  • {o}")
    print("\nWork Products:")
    for w in info["work_products"]:
        print(f"  • {w}")
    print("\nBase Practices:")
    for b in info["base_practices"]:
        print(f"  • {b}")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    _print_banner()

    parser = argparse.ArgumentParser(
        prog="aspice",
        description="ASPICE v4.0 Capability Checker — RAG Agent CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # chat
    sub.add_parser("chat", help="Interactive Q&A with the ASPICE agent")

    # assess
    p_assess = sub.add_parser("assess", help="Assess a single process capability level")
    p_assess.add_argument("--process", required=True, help="Process ID (e.g. SWE.1)")
    p_assess.add_argument("--ratings", help='JSON PA ratings e.g. \'{"PA 1.1":"F","PA 2.1":"L"}\'')

    # roadmap
    p_rm = sub.add_parser("roadmap", help="Generate improvement roadmap")
    p_rm.add_argument("--target", type=int, default=3, help="Target capability level (1-5)")
    p_rm.add_argument("--processes", nargs="+", required=True, help="Process IDs to include")

    # levels
    sub.add_parser("levels", help="List all ASPICE capability levels and process attributes")

    # info
    p_info = sub.add_parser("info", help="Show detailed info for an ASPICE process")
    p_info.add_argument("--process", required=True, help="Process ID (e.g. MAN.3)")

    args = parser.parse_args()

    dispatch = {
        "chat": cmd_chat,
        "assess": cmd_assess,
        "roadmap": cmd_roadmap,
        "levels": cmd_levels,
        "info": cmd_info,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
