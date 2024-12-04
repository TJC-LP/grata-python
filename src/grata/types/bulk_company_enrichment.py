# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .company_detailed import CompanyDetailed

__all__ = ["BulkCompanyEnrichment"]


class BulkCompanyEnrichment(BaseModel):
    companies: Optional[List[CompanyDetailed]] = None

    errors: Optional[List[str]] = None
