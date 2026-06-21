# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RunListItem"]


class RunListItem(BaseModel):
    """One check execution in a list.

    Location is exposed as structured
    `provider`/`region`/`location` fields rather than infrastructure
    internals; the row carries cheap boolean flags and a short
    `error_summary` (null on a passing run). For the full record
    (metadata + downloadable artifacts), fetch `GET /v1/runs/{id}`.
    """

    id: str
    """Run typeid (`run_<26-char base32 UUIDv7>`)."""

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

    error_summary: Optional[str] = None
    """Short failure summary; null on a passing run."""

    location: Optional[str] = None
    """Human-readable location label (e.g. `Falkenstein, DE`). Null when unresolved."""

    provider: Optional[str] = None
    """Cloud provider that ran the check (e.g.

    `hetzner`, `ovh`). Null when unresolved.
    """

    region: Optional[str] = None
    """Provider-native region id (e.g. `fsn1`, `gra7`). Null when unresolved."""
