# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    check_id: str
    """Filter to a single check (UUID; matches `Check.id`)."""

    cursor: str
    """Opaque pagination token from the previous page's `next_cursor`."""

    limit: int
    """Page size; defaults to 50, max 200."""

    location: str
    """Filter to a single provider-native region id (e.g. `fsn1`)."""

    since: int
    """Lower bound on `started_at_unix_ms` (inclusive)."""

    status: Literal["PASS", "FAIL", "ERROR", "TIMEOUT"]
    """Filter to a single execution status."""

    until: int
    """Upper bound on `started_at_unix_ms` (inclusive)."""
