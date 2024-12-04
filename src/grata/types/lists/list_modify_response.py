# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ListModifyResponse", "NotProcessed", "Processed", "Result", "ResultCompany"]


class NotProcessed(BaseModel):
    companies: Optional[List[str]] = None
    """The list of primary domains not added to or removed from the list."""

    count: Optional[int] = None
    """The number of companies not added to or removed from the list."""


class Processed(BaseModel):
    companies: Optional[List[str]] = None
    """The list of primary domains added to or removed from the list."""

    count: Optional[int] = None
    """The number of companies added to or removed from the list."""


class ResultCompany(BaseModel):
    domain: Optional[str] = None
    """The domain associated with the inputted value."""

    uid: Optional[str] = None
    """The UID associated with the inputted value."""


class Result(BaseModel):
    company: Optional[ResultCompany] = None

    input: Optional[str] = None
    """The inputted domain or UID."""

    processed: Optional[bool] = None
    """Indicates whether the input was processed."""


class ListModifyResponse(BaseModel):
    not_processed: Optional[NotProcessed] = None

    processed: Optional[Processed] = None

    results: Optional[List[Result]] = None
