# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .alert_channel import AlertChannel
from .maintenance_window import MaintenanceWindow

__all__ = ["AlertConfig"]


class AlertConfig(BaseModel):
    channels: List[AlertChannel]

    consecutive_failures_threshold: int
    """
    Number of consecutive globally-failing observations (after M-of-N consensus
    collapses per-location status) required before an incident fires. Default = 1 =
    "alert on first globally-failing observation."
    """

    consensus_m: int
    """M-of-N consensus rule denominator (expected total location count).

    When fewer than `consensus_m` locations have observations, the evaluator falls
    back to "any failing = failing" so brand-new checks don't miss outages.
    """

    consensus_n: int
    """M-of-N consensus rule numerator.

    The evaluator considers the check globally-failing only when at least this many
    locations are reporting fail concurrently.
    """

    enabled: bool
    """When false, the evaluator skips this check entirely."""

    account_id: Optional[str] = None
    """Server-set; ignored on write."""

    check_id: Optional[str] = None
    """Server-set; ignored on write."""

    created_at: Optional[datetime] = None

    maintenance_windows: Optional[List[MaintenanceWindow]] = None
    """
    Absolute-time windows during which the evaluator suppresses dispatch but still
    updates state. Cron-style recurring windows are a future enhancement.
    """

    updated_at: Optional[datetime] = None
