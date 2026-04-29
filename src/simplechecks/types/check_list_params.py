# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CheckListParams"]


class CheckListParams(TypedDict, total=False):
    limit: int
    """Max number of checks to return. Defaults to 100; the server caps further."""

    offset: int
    """Number of checks to skip. Pass the `next_offset` from the previous page."""
