# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Run"]


class Run(BaseModel):
    """A single check execution.

    Runs are written by the garrison that
    executed the check; CC reads them from S3-resident parquet files
    for read-only public exposure here.
    """

    id: str
    """Run typeid (`run_<26-char base32 UUIDv7>`)."""

    check_id: str
    """UUID of the parent check (matches `Check.id`)."""

    check_name: str

    duration_ms: int

    garrison_id: str

    instance_id: str

    node_name: str

    started_at_unix_ms: int
    """Execution start time in unix milliseconds (UTC)."""

    status: Literal["PASS", "FAIL", "ERROR", "TIMEOUT"]

    type: str
    """Check type (`http`, `tcp`, `dns`, ...)."""

    error_message: Optional[str] = None

    metadata: Optional[str] = None
    """Per-check-type metadata blob, JSON-encoded as a string."""
