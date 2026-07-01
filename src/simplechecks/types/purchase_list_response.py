# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .purchase import Purchase

__all__ = ["PurchaseListResponse"]


class PurchaseListResponse(BaseModel):
    purchases: List[Purchase]
