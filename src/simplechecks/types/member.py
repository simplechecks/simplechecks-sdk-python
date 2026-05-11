# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Member"]


class Member(BaseModel):
    """A user's membership in the caller's account."""

    created_at: datetime
    """When the member joined this account."""

    email: str

    role: Literal["owner", "admin", "member", "billing", "viewer"]

    user_id: str
    """UUID of the member."""
