# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .check import Check
from .._models import BaseModel

__all__ = ["CheckListResponse"]


class CheckListResponse(BaseModel):
    checks: List[Check]

    next_offset: Optional[int] = None
    """
    Offset to pass on the next request to continue pagination. Zero (or absent) when
    there's no more data.
    """
