# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AlertReplaceParams"]


class AlertReplaceParams(TypedDict, total=False):
    consecutive_failures_threshold: Required[int]
    """
    Number of consecutive globally-failing observations (after M-of-N consensus
    collapses per-location status) required before an incident fires. Default = 1 =
    "alert on first globally-failing observation."
    """

    consensus_m: Required[int]
    """M-of-N consensus rule denominator (expected total location count).

    When fewer than `consensus_m` locations have observations, the evaluator falls
    back to "any failing = failing" so brand-new checks don't miss outages.
    """

    consensus_n: Required[int]
    """M-of-N consensus rule numerator.

    The evaluator considers the check globally-failing only when at least this many
    locations are reporting fail concurrently.
    """

    enabled: Required[bool]
    """When false, the evaluator skips this check entirely."""

    account_id: str
    """Server-set; ignored on write."""

    check_id: str
    """Server-set; ignored on write."""
