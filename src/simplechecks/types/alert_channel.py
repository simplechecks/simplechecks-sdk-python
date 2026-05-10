# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AlertChannel"]


class AlertChannel(BaseModel):
    target: str
    """Channel-specific destination.

    URL for the webhook flavors (slack/discord/teams/webhook), email address for
    `email`, integration key for `pagerduty`, API key for `opsgenie`.
    """

    type: Literal["email", "slack", "discord", "teams", "webhook", "pagerduty", "opsgenie"]

    config: Optional[Dict[str, object]] = None
    """Type-specific options. Optional."""
