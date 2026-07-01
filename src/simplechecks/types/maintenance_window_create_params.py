# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MaintenanceWindowCreateParams"]


class MaintenanceWindowCreateParams(TypedDict, total=False):
    duration_ms: Required[int]
    """Window duration in milliseconds; must be positive."""

    name: Required[str]

    schedule_kind: Required[Literal["one_time", "recurring"]]

    start_unix_ms: Required[int]

    check_ids: SequenceNotStr[str]
    """Raw check UUIDs to target (must belong to your account)."""

    check_tags: SequenceNotStr[str]

    repeat_ends_unix_ms: int
    """Valid only for a recurring window."""

    repeat_interval: int
    """Valid only for a recurring window; must be positive."""

    repeat_unit: Literal["DAY", "WEEK", "MONTH"]
    """Valid only for a recurring window."""

    timezone: str
    """IANA timezone name. Defaults to UTC when omitted."""
