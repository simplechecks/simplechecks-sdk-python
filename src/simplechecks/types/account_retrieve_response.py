# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse"]


class AccountRetrieveResponse(BaseModel):
    """Account profile + cached billing balance. Returned by GET /v1/account."""

    balance: int
    """Cached run-credit balance, in run-credit units."""

    created_at: datetime

    name: str

    paused: bool
    """True when execution is paused (e.g. balance exhausted)."""

    plan: str
    """Billing plan identifier."""

    slug: str
    """Renameable URL-friendly handle.

    Display only — never use as a system identifier.
    """

    typeid: str
    """Stable account identifier (`acct_<typeid>`).

    Used in API responses and audit logs.
    """
