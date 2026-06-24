# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AlertSubscriptionListParams"]


class AlertSubscriptionListParams(TypedDict, total=False):
    channel_id: str
    """Filter to subscriptions for this channel (`chan_<typeid>`)."""

    check_id: str
    """Filter to subscriptions for this check (raw check UUID)."""

    cursor: str
    """Opaque pagination token from the previous page's `next_cursor`."""

    limit: int
