# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunAggregatesParams"]


class RunAggregatesParams(TypedDict, total=False):
    bucket: Literal["minute"]
    """Bucket size. Only `minute` accepted today."""

    check_id: str
    """Filter to one check."""

    from_: Annotated[int, PropertyInfo(alias="from")]
    """Inclusive lower bound, unix-millis. Defaults to `now() - 1h`."""

    limit: int
    """Maximum number of rows. Default 1000; hard cap 5000."""

    location: str
    """Filter to one location (e.g. `hetzner`, `ovh`)."""

    to: int
    """Exclusive upper bound, unix-millis. Defaults to `now() + 1m`."""
