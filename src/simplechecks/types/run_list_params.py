# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    check_id: str
    """Filter to a single check (UUID; matches `Check.id`)."""

    limit: int

    offset: int

    since: int
    """Lower bound on `started_at_unix_ms`. Server clamps to a 7-day window."""

    status: Literal["PASS", "FAIL", "ERROR", "TIMEOUT"]
    """Filter to a single execution status."""
