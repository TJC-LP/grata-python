# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .list_response import ListResponse

__all__ = ["ListSearchResponse"]


class ListSearchResponse(BaseModel):
    count: Optional[int] = None
    """Number of lists in the results"""

    page: Optional[int] = None
    """Current page of results"""

    pages: Optional[int] = None
    """Number of pages of results"""

    results: Optional[List[ListResponse]] = None
