# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AlertSubscriptionCreateParams"]


class AlertSubscriptionCreateParams(TypedDict, total=False):
    channel_id: Required[str]
    """The channel to bind in `chan_<typeid>` form (must belong to your account)."""

    check_id: Required[str]
    """The check to subscribe (must belong to your account)."""

    notify_on_failure: bool
    """Defaults to true when omitted."""

    notify_on_recovery: bool
    """Defaults to true when omitted."""
