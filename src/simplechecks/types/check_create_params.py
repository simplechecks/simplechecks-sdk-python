# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CheckCreateParams"]


class CheckCreateParams(TypedDict, total=False):
    enabled: Required[bool]

    location: Required[str]
    """Provider-specific region/location."""

    name: Required[str]

    provider: Required[str]
    """Cloud provider (`mock`, `ec2`, `ovh`, `azure`, `gcp`, `hetzner`)."""

    schedule: Required[str]

    target_url: Required[str]

    type: Required[str]

    artifact_url: str

    config: Dict[str, object]

    timeout_ms: int
