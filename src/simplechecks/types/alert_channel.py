# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AlertChannel"]


class AlertChannel(BaseModel):
    """A first-class, reusable alert channel.

    Referenced by many checks
    through alert subscriptions. The `target` secret is always
    returned masked (`***<last4>`).
    """

    id: str
    """Channel id in `chan_<typeid>` form."""

    account_typeid: str
    """Owning account's `acct_<typeid>`. Read-only."""

    created_at: datetime

    name: str
    """Account-unique display name."""

    target: str
    """Masked destination secret (`***<last4>`).

    The raw value is write-only and never returned.
    """

    type: Literal["slack", "discord", "teams", "webhook", "pagerduty", "opsgenie", "email"]

    updated_at: datetime

    config: Optional[Dict[str, object]] = None
    """Type-specific options. Optional."""
