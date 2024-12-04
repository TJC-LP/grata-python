# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BulkEnrichParams"]


class BulkEnrichParams(TypedDict, total=False):
    authorization: Required[Annotated[str, PropertyInfo(alias="Authorization")]]

    company_uids: List[str]
    """An array of unique alphanumeric Grata IDs for the companies."""

    domains: List[str]
    """An array of domains for the companies being enriched."""