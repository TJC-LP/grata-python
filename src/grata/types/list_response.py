# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ListResponse"]


class ListResponse(BaseModel):
    company_count: Optional[int] = None
    """The number of companies in the list"""

    created_date: Optional[str] = None
    """The date the list was created"""

    list_uid: Optional[str] = None
    """UID of the list"""

    name: Optional[str] = None
    """Name of the list"""

    updated_date: Optional[str] = None
    """The date the list was last updated"""
