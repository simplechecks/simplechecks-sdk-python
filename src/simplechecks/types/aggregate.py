# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Aggregate"]


class Aggregate(BaseModel):
    account_id: str

    bucket_end_unix_ms: int
    """Exclusive bucket end (= start + 60 000 ms today)."""

    bucket_start_unix_ms: int
    """Inclusive bucket start, unix-millis, minute-aligned to UTC."""

    check_id: str

    duration_avg_ms: int
    """Server-computed average from sum/count. Zero when the bucket has no runs."""

    error_count: int

    fail_count: int

    location: str
    """Garrison cloud / region label (e.g. `hetzner`, `ovh`, `aws`)."""

    pass_count: int

    timeout_count: int

    total_count: int
    """Sum of all four status counts.

    Convenience for clients that compute uptime as `pass_count / total_count`.
    """

    duration_max_ms: Optional[int] = None

    duration_min_ms: Optional[int] = None
