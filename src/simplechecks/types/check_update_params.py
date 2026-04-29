# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["CheckUpdateParams"]


class CheckUpdateParams(TypedDict, total=False):
    artifact_url: str

    config: Dict[str, object]

    enabled: bool

    name: str

    schedule: str

    target_url: str

    timeout_ms: int

    type: str
