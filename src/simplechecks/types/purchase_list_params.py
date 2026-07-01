# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PurchaseListParams"]


class PurchaseListParams(TypedDict, total=False):
    limit: int
    """Page size.

    Server applies a default of 100 when omitted or when set to 0; values above the
    server cap are clamped.
    """

    offset: int
    """Pagination offset within the newest-first list."""
