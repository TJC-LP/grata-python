# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .company import Company
from .._models import BaseModel

__all__ = ["SearchSearchResponse"]


class SearchSearchResponse(BaseModel):
    companies: List[Company]

    count: int
    """Total number of items."""

    page_token: str
    """Token for pagination."""
