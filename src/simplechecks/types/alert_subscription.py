# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AlertSubscription"]


class AlertSubscription(BaseModel):
    """
    A binding between one check and one alert channel, carrying the
    per-binding notify flags. The same channel can be subscribed by
    many checks, each with its own flags.
    """

    id: str
    """Subscription id in `asub_<typeid>` form."""

    account_typeid: str
    """Owning account's `acct_<typeid>`. Read-only."""

    channel_id: str
    """The bound channel's id in `chan_<typeid>` form."""

    check_id: str
    """The subscribed check's id."""

    created_at: datetime

    notify_on_failure: bool
    """When true, an incident-started event dispatches to this channel."""

    notify_on_recovery: bool
    """When true, an incident-recovered event dispatches to this channel."""

    updated_at: datetime
