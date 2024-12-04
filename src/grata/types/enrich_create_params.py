# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EnrichCreateParams"]


class EnrichCreateParams(TypedDict, total=False):
    company_uid: str
    """Unique alphanumeric Grata ID for the company (case-sensitive)."""

    domain: str
    """Domain of the company being enriched.

    Protocol and path can be included. If both the domain and company_uid are
    included, the domain will be referenced.
    """