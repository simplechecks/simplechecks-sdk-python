# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .incident import Incident

__all__ = ["IncidentListResponse"]


class IncidentListResponse(BaseModel):
    incidents: List[Incident]

    next_offset: Optional[int] = None
    """Offset to pass on the next request. Zero (or absent) when there's no more data."""
