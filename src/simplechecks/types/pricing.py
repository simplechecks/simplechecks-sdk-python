# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["Pricing", "CheckType", "Multiplier"]


class CheckType(BaseModel):
    """
    One check type's per-run weight (compute + artifact egress),
    pre-multiplier.
    """

    check_type: str
    """Check type identifier."""

    egress_weight: int
    """The artifact-egress portion of `weight` (0 for non-artifact types).

    Surfaced so a UI can label the artifact-retrieval cost of a browser/playwright
    run.
    """

    weight: int
    """Per-run weight, compute plus artifact egress (pre-multiplier)."""


class Multiplier(BaseModel):
    """One (provider, location) cost multiplier."""

    location: str
    """Provider-native location id; empty for a provider-wide default."""

    multiplier_milli: int
    """Multiplier × 1000 (e.g. 500 = 0.5×, the cheap-provider wedge)."""

    provider: str


class Pricing(BaseModel):
    """The active token-pricing table.

    cost(run) =
    `floor(weight × multiplier_milli / 1000)`, multiplier resolving
    `(provider, location)` → `(provider, "")` → `1.0` (1000 milli).
    """

    check_types: List[CheckType]

    multipliers: List[Multiplier]
