# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Purchase"]


class Purchase(BaseModel):
    """One row of the customer's Stripe Checkout bundle purchase
    history.

    Tokens are credited at fulfillment time; pending and
    failed rows reflect Checkout sessions that did not complete.
    """

    id: str
    """Server-side purchase id."""

    amount_cents: int
    """Customer-paid amount in the smallest currency unit (e.g., USD cents)."""

    bundle_sku: str
    """Bundle identifier (e.g., `starter`, `growth`, `scale`, `team`)."""

    created_at: datetime
    """When the Checkout session was minted."""

    currency: str
    """ISO 4217 currency code (e.g., `usd`)."""

    status: Literal["pending", "fulfilled", "failed"]

    stripe_session_id: str
    """Stripe Checkout session that originated this purchase."""

    tokens: int
    """Total tokens credited on fulfillment (includes any bonus)."""

    fulfilled_at: Optional[datetime] = None
    """
    When the payment landed and tokens were credited; absent for non-fulfilled rows.
    """

    receipt_url: Optional[str] = None
    """Stripe-hosted receipt PDF URL.

    Absent for in-flight purchases and for fulfilled purchases whose payment event
    did not surface a receipt (e.g., asynchronous payment methods).
    """
