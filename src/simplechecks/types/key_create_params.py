# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """Operator/customer-facing label."""

    scopes: SequenceNotStr[str]
    """Scope strings (e.g.

    `checks:read`). Empty = server applies its default set. Unknown scopes return
    InvalidArgument.
    """
