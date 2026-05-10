# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IncidentListParams"]


class IncidentListParams(TypedDict, total=False):
    limit: int
    """Max number of incidents to return. Defaults to 50; server caps at 500."""

    offset: int
    """Number of incidents to skip. Pass the `next_offset` from the previous page."""
