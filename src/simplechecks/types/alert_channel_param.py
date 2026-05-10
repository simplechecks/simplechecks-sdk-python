# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertChannelParam"]


class AlertChannelParam(TypedDict, total=False):
    target: Required[str]
    """Channel-specific destination.

    URL for the webhook flavors (slack/discord/teams/webhook), email address for
    `email`, integration key for `pagerduty`, API key for `opsgenie`.
    """

    type: Required[Literal["email", "slack", "discord", "teams", "webhook", "pagerduty", "opsgenie"]]

    config: Dict[str, object]
    """Type-specific options. Optional."""
