# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertReplaceParams", "Channel", "MaintenanceWindow"]


class AlertReplaceParams(TypedDict, total=False):
    channels: Required[Iterable[Channel]]

    consecutive_failures_threshold: Required[int]
    """
    Number of consecutive globally-failing observations (after M-of-N consensus
    collapses per-location status) required before an incident fires. Default = 1 =
    "alert on first globally-failing observation."
    """

    consensus_m: Required[int]
    """M-of-N consensus rule denominator (expected total location count).

    When fewer than `consensus_m` locations have observations, the evaluator falls
    back to "any failing = failing" so brand-new checks don't miss outages.
    """

    consensus_n: Required[int]
    """M-of-N consensus rule numerator.

    The evaluator considers the check globally-failing only when at least this many
    locations are reporting fail concurrently.
    """

    enabled: Required[bool]
    """When false, the evaluator skips this check entirely."""

    account_id: str
    """Server-set; ignored on write."""

    check_id: str
    """Server-set; ignored on write."""

    maintenance_windows: Iterable[MaintenanceWindow]
    """
    Absolute-time windows during which the evaluator suppresses dispatch but still
    updates state. Cron-style recurring windows are a future enhancement.
    """


class Channel(TypedDict, total=False):
    target: Required[str]
    """Channel-specific destination.

    URL for the webhook flavors (slack/discord/teams/webhook), email address for
    `email`, integration key for `pagerduty`, API key for `opsgenie`.
    """

    type: Required[Literal["email", "slack", "discord", "teams", "webhook", "pagerduty", "opsgenie"]]

    config: Dict[str, object]
    """Type-specific options. Optional."""


class MaintenanceWindow(TypedDict, total=False):
    end_unix_ms: Required[int]

    start_unix_ms: Required[int]
