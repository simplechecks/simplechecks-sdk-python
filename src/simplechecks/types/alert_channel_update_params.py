# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["AlertChannelUpdateParams"]


class AlertChannelUpdateParams(TypedDict, total=False):
    config: Dict[str, object]

    name: str

    target: str

    type: Literal["slack", "discord", "teams", "webhook", "pagerduty", "opsgenie", "email"]
