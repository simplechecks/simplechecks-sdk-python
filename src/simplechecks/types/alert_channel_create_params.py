# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertChannelCreateParams"]


class AlertChannelCreateParams(TypedDict, total=False):
    name: Required[str]

    target: Required[str]
    """Destination secret.

    URL for the webhook flavors (slack/discord/teams/webhook), email address for
    `email`, integration key for `pagerduty`, API key for `opsgenie`. URL-bearing
    types are SSRF-filtered.
    """

    type: Required[Literal["slack", "discord", "teams", "webhook", "pagerduty", "opsgenie", "email"]]

    config: Dict[str, object]
