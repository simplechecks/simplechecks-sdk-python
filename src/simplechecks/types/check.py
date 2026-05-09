# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Check"]


class Check(BaseModel):
    id: str

    account_typeid: str
    """Owning account's `acct_<typeid>`. Read-only."""

    created_at: datetime

    enabled: bool

    garrison_id: str
    """Garrison the check is bound to. Server-assigned."""

    name: str

    schedule: str
    """Cron expression; minute granularity."""

    target_url: str

    timeout_ms: int

    type: str
    """Check type. Currently only `http` is publicly documented."""

    updated_at: datetime

    artifact_url: Optional[str] = None
    """Optional artifact reference (e.g. uploaded Playwright bundle)."""

    config: Optional[Dict[str, object]] = None
    """Per-check-type configuration blob. Opaque on the wire."""

    location: Optional[str] = None
    """Region/location on read responses is empty; populated on create requests only."""

    provider: Optional[str] = None
    """Cloud provider on read responses is empty; populated on create requests only."""
