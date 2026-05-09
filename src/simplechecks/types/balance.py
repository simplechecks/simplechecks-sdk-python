# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Balance"]


class Balance(BaseModel):
    balance: int
    """Cached run-credit balance."""

    paused: bool
    """True when execution is paused (e.g. balance exhausted)."""
