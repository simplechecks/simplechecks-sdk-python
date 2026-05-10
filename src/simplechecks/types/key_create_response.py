# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["KeyCreateResponse"]


class KeyCreateResponse(BaseModel):
    key_id: str

    plaintext_token: str
    """Full `sc_live_…` token.

    Returned once; not retrievable later. Clients MUST persist this before
    discarding the response.
    """

    prefix: str
