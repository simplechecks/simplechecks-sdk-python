# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RunDetail", "Artifact"]


class Artifact(BaseModel):
    """One downloadable artifact for a run."""

    kind: Literal["screenshot", "trace", "har"]
    """Artifact kind (closed set)."""

    url: str
    """Opaque, webapp-relative download path (`/v1/runs/{id}/artifacts/{kind}`)."""


class RunDetail(BaseModel):
    """
    The full record for one check execution: the list fields plus the
    run's `metadata` (a JSON object) and the set of downloadable
    `artifacts`. Location is structured; no infrastructure identifiers
    are exposed.
    """

    id: str
    """Run typeid (`run_<26-char base32 UUIDv7>`)."""

    artifacts: List[Artifact]
    """Downloadable artifacts for this run (empty when none)."""

    check_id: str
    """UUID of the parent check (matches `Check.id`)."""

    check_name: str

    duration_ms: int

    has_errors: bool

    has_failures: bool

    started_at_unix_ms: int
    """Execution start time in unix milliseconds (UTC)."""

    status: Literal["PASS", "FAIL", "ERROR", "TIMEOUT"]

    type: str
    """Check type (`http`, `tcp`, `dns`, ...)."""

    degraded: Optional[bool] = None
    """Reserved; always null at this version."""

    error_message: Optional[str] = None
    """Full failure message; null on a passing run."""

    location: Optional[str] = None
    """Human-readable location label. Null when unresolved."""

    metadata: Optional[Dict[str, object]] = None
    """Per-check-type metadata as a JSON object; null when absent."""

    provider: Optional[str] = None
    """Cloud provider that ran the check. Null when unresolved."""

    region: Optional[str] = None
    """Provider-native region id. Null when unresolved."""
