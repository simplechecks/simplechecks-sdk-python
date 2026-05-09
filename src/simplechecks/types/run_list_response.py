# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .run import Run
from .._models import BaseModel

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    runs: List[Run]
