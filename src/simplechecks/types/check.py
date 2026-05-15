# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
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
    """Legacy: the first location's provider-native id.

    Same back-compat caveats as `provider`. Consult `locations`.
    """

    locations: Optional[List[str]] = None
    """All locations the check runs from, in wire form (`provider:location`, e.g.

    `aws:us-east-1`). Element 0 is the deterministic "primary" — order matches
    creation.
    """

    provider: Optional[str] = None
    """Legacy: the first location's provider, mirrors `locations[0]` split.

    Empty on read for multi-location checks (consult `locations` instead). Kept for
    one release cycle of SDK back-compat.
    """
