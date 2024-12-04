# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CompanyModifyParams"]


class CompanyModifyParams(TypedDict, total=False):
    action: Literal["add", "remove"]
    """Action to perform on the list."""

    domains: List[str]
    """Domains to add or remove from a list (max of 500 permitted per call)."""

    uids: List[str]
    """
    Grata company UIDs to add or remove from a list (max of 500 permitted per call).
    """
