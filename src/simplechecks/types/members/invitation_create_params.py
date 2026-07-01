# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InvitationCreateParams"]


class InvitationCreateParams(TypedDict, total=False):
    email: Required[str]

    role: Required[Literal["owner", "admin", "member", "billing", "viewer"]]
