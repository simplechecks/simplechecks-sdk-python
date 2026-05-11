# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Invitation"]


class Invitation(BaseModel):
    """A pending invitation to join the account."""

    id: str

    created_at: datetime

    email: str

    expires_at: datetime

    invited_by_user_id: str

    role: Literal["owner", "admin", "member", "billing", "viewer"]

    token: Optional[str] = None
    """Random URL-safe token.

    Only returned at creation time (POST /v1/invitations); GET responses omit this
    field.
    """

    accept_url_path: Optional[str] = None
    """Convenience: the relative path the webapp routes to for redemption.

    Only present on creation responses.
    """
