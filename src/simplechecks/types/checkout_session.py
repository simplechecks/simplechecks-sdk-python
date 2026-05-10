# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CheckoutSession"]


class CheckoutSession(BaseModel):
    checkout_url: str
    """Stripe-hosted page the customer pays on."""

    stripe_session_id: str

    expires_at: Optional[datetime] = None
