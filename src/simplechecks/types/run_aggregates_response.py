# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .aggregate import Aggregate

__all__ = ["RunAggregatesResponse"]


class RunAggregatesResponse(BaseModel):
    aggregates: List[Aggregate]
