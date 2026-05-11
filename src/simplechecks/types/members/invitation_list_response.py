# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..invitation import Invitation

__all__ = ["InvitationListResponse"]


class InvitationListResponse(BaseModel):
    invitations: List[Invitation]
