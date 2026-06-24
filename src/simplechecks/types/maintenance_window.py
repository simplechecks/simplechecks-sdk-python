# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MaintenanceWindow"]


class MaintenanceWindow(BaseModel):
    """
    A maintenance window that pauses execution of its targeted
    checks for the scheduled interval(s). The DST-correct occurrence
    expansion is performed by the control plane; this resource
    carries the stored schedule shape plus its explicit targeting.
    """

    id: str
    """Window id in `mwin_<typeid>` form."""

    account_typeid: str
    """Owning account's `acct_<typeid>`. Read-only."""

    check_ids: List[str]
    """Raw UUIDs of the targeted checks."""

    check_tags: List[str]
    """Reserved for tag-based targeting; accepted but not yet consumed."""

    created_at: datetime

    duration_ms: int
    """Window duration in milliseconds (> 0)."""

    name: str

    schedule_kind: Literal["one_time", "recurring"]

    start_unix_ms: int
    """First occurrence start, Unix epoch milliseconds."""

    timezone: str
    """IANA timezone name (e.g. "America/Chicago"). Defaults to UTC."""

    updated_at: datetime

    repeat_ends_unix_ms: Optional[int] = None
    """Recurrence end bound, Unix epoch ms; recurring only."""

    repeat_interval: Optional[int] = None
    """Recurrence interval (e.g. every N units); recurring only."""

    repeat_unit: Optional[Literal["DAY", "WEEK", "MONTH"]] = None
    """Recurrence unit; present only for a recurring window."""
