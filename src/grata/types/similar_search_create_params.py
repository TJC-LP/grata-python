# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = [
    "SimilarSearchCreateParams",
    "Headquarters",
    "HeadquartersExclude",
    "HeadquartersInclude",
    "IndustryClassifications",
    "Lists",
    "TermsInclude",
    "TermsIncludeGroup",
]


class SimilarSearchCreateParams(TypedDict, total=False):
    business_models: List[str]

    company_uid: str
    """Alphanumeric Grata ID for the company (case-sensitive)."""

    domain: str
    """Domain of the company for similar search.

    Protocol and path can be included. If both the domain and company_uid are
    specified, domain will be referenced.
    """

    employees_change: Iterable[float]

    employees_change_time: Literal["month", "quarter", "six_month", "annual"]

    employees_on_professional_networks_range: Iterable[int]

    end_customer: List[str]

    funding_size: Iterable[int]

    funding_stage: List[str]

    grata_employees_estimates_range: Iterable[int]

    headquarters: Headquarters

    industry_classifications: IndustryClassifications

    is_funded: bool

    lists: Lists

    ownership: List[str]

    page_token: str
    """Page token used for pagination."""

    terms_exclude: List[str]

    terms_include: TermsInclude

    year_founded: Iterable[int]


class HeadquartersExclude(TypedDict, total=False):
    city: str

    country: str

    state: str


class HeadquartersInclude(TypedDict, total=False):
    city: str

    country: str

    example: object

    state: str


class Headquarters(TypedDict, total=False):
    exclude: Iterable[HeadquartersExclude]

    include: Iterable[HeadquartersInclude]


class IndustryClassifications(TypedDict, total=False):
    exclude: Iterable[float]

    include: Iterable[float]


class Lists(TypedDict, total=False):
    exclude: List[str]

    include: List[str]


class TermsIncludeGroup(TypedDict, total=False):
    terms: List[str]

    terms_depth: Literal["core", "mention"]

    terms_operator: Literal["any", "all"]


class TermsInclude(TypedDict, total=False):
    group_operator: Literal["any", "all"]

    groups: Iterable[TermsIncludeGroup]
