# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["MaintenanceWindowUpdateParams"]


class MaintenanceWindowUpdateParams(TypedDict, total=False):
    check_ids: SequenceNotStr[str]

    check_tags: SequenceNotStr[str]

    duration_ms: int

    name: str

    repeat_ends_unix_ms: int

    repeat_interval: int

    repeat_unit: Literal["DAY", "WEEK", "MONTH"]

    schedule_kind: Literal["one_time", "recurring"]

    start_unix_ms: int

    timezone: str
