# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MaintenanceWindowParam"]


class MaintenanceWindowParam(TypedDict, total=False):
    end_unix_ms: Required[int]

    start_unix_ms: Required[int]
