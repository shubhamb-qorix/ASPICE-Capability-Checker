"""src package init — exposes the primary public API."""

from .rag_engine import AspiceAgent, assess_capability_level

__all__ = ["AspiceAgent", "assess_capability_level"]
