# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CheckCreateParams"]


class CheckCreateParams(TypedDict, total=False):
    enabled: Required[bool]

    name: Required[str]

    schedule: Required[str]

    target_url: Required[str]

    type: Required[str]

    artifact_url: str

    config: Dict[str, object]

    location: str
    """Legacy; see `provider`."""

    locations: SequenceNotStr[str]
    """
    Preferred: array of wire-form ids (`aws:us-east-1`). Element 0 is the
    deterministic primary. Each entry must be in the deployment catalog returned by
    `GET /v1/locations`.
    """

    provider: str
    """Legacy single-location shape.

    Translated server-side to `locations=[<provider>:<location>]`. Kept for one
    release cycle.
    """

    timeout_ms: int
