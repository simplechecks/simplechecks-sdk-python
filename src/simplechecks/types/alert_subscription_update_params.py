# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AlertSubscriptionUpdateParams"]


class AlertSubscriptionUpdateParams(TypedDict, total=False):
    notify_on_failure: bool

    notify_on_recovery: bool
