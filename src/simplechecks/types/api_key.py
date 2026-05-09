# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    """An account-scoped personal access token (PAT).

    The plaintext
    token never appears here; it's only returned by POST /v1/keys
    at mint time.
    """

    id: str
    """Server-side key id (used for revoke)."""

    account_typeid: str

    created_at: datetime

    name: str
    """Operator/customer-facing label."""

    prefix: str
    """Logging-safe visible portion (e.g. `sc_live_xxx`)."""

    scopes: List[str]

    last_used_at: Optional[datetime] = None

    revoked_at: Optional[datetime] = None
