# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, TypeAlias

from .owner import Owner
from .._models import BaseModel

__all__ = [
    "Company",
    "Classifications",
    "ClassificationsIndustryClassification",
    "ClassificationsSoftwareIndustry",
    "Conferences",
    "ConferencesConference",
    "Contacts",
    "ContactsContact",
    "Domain",
    "EmployeeLocationBreakdown",
    "EmployeesGrowth",
    "Investors",
    "InvestorsInvestors",
    "Locations",
    "LocationsLocation",
    "LocationsLocationGreaterRegion",
]


class ClassificationsIndustryClassification(BaseModel):
    industry_code: str
    """Industry code."""

    industry_name: str
    """Industry name."""


class ClassificationsSoftwareIndustry(BaseModel):
    industry_code: str
    """Software industry code."""

    industry_name: str
    """Software industry name."""


class Classifications(BaseModel):
    industry_classifications: List[ClassificationsIndustryClassification]
    """Industry classifications for the company."""

    software_industries: List[ClassificationsSoftwareIndustry]
    """Software industry classifications for the company."""


class ConferencesConference(BaseModel):
    company_count: int
    """Total count of companies attending the conference."""

    end_date: date
    """End date of the conference (YYYY-MM-DD)."""

    location: str
    """Location of the conference."""

    name: str
    """Name of the conference."""

    start_date: date
    """Start date of the conference (YYYY-MM-DD)."""

    url: str
    """Link to the conference."""


class Conferences(BaseModel):
    conferences: List[ConferencesConference]
    """List of conferences."""

    count: int
    """Total count of all conferences."""


class ContactsContact(BaseModel):
    name: str
    """Name of the contact."""

    title: str
    """Title of the contact."""

    work_email: str
    """Work email of the contact."""

    age: Optional[int] = None
    """Age of contact."""

    email_deliverability: Optional[str] = None
    """Email Deliverability of the contact's email."""

    socials_facebook: Optional[str] = None
    """Link to the contact's Facebook page."""

    socials_linkedin: Optional[str] = None
    """Link to the contact's LinkedIn page."""

    socials_twitter: Optional[str] = None
    """Link to the contact's Twitter page."""


class Contacts(BaseModel):
    contacts: List[ContactsContact]
    """List of contacts."""

    count: int
    """Total count of all contacts."""


class Domain(BaseModel):
    domain: str
    """Domain of a company."""

    domain_type: Literal[
        "Primary",
        "Product",
        "Business unit",
        "Redirect",
        "Foreign language",
        "Corporate",
        "Blog",
        "Blacklisted domain",
        "Secondary",
    ]
    """The type of domain."""

    status: float
    """Indicates if this domain is active.

    0 indicates an active domain, 1 indicates an inactive domain.
    """


class EmployeeLocationBreakdown(BaseModel):
    confidence: str
    """Confidence score of the prediction."""

    country: str
    """Country where the employees are located."""

    country_percentage: float
    """Percentage of the employees located in the specified country."""


class EmployeesGrowth(BaseModel):
    percentage_one_month: float
    """1 month growth rate as a percentage."""

    percentage_one_year: float
    """Annual growth rate as a percentage."""

    percentage_six_month: float
    """6 month growth rate as a percentage."""

    percentage_three_month: float
    """3 month growth rate as a percentage."""


class InvestorsInvestors(BaseModel):
    id: str
    """Platform ID for the investor."""

    domain: str
    """Domain of the investor."""

    name: str
    """Name of the investor."""


Investors: TypeAlias = Union[str, InvestorsInvestors]


class LocationsLocationGreaterRegion(BaseModel):
    name: Optional[str] = None
    """Name of the greater region."""


class LocationsLocation(BaseModel):
    city_name: str
    """Name of the city of the location."""

    country_iso2: str
    """Two-digit country abbreviation."""

    continent_name: Optional[str] = None
    """Name of the continent of the location."""

    country_iso3: Optional[str] = None
    """Three-digit country abbreviation."""

    country_name: Optional[str] = None
    """Name of the country for the location."""

    greater_regions: Optional[List[LocationsLocationGreaterRegion]] = None
    """List of the greater regions encompassing the location."""

    house_number: Optional[str] = None
    """House number for the location."""

    latitude: Optional[float] = None
    """Latitude for the location."""

    location_type: Optional[str] = None
    """Indicates if the location is the HQ or location of business."""

    longitude: Optional[float] = None
    """Longitude for the location."""

    macro_region: Optional[str] = None
    """Macro region for the location."""

    micro_region: Optional[str] = None
    """Micro region for the location."""

    postal_code: Optional[str] = None
    """Postal code of location."""

    raw_address: Optional[str] = None
    """The location's full address."""

    region_iso: Optional[str] = None
    """Region abbreviation of the location."""

    region_name: Optional[str] = None
    """Name of the region for the location."""

    street: Optional[str] = None
    """Street name of the location."""


class Locations(BaseModel):
    locations: List[LocationsLocation]
    """List of locations."""

    total: int
    """Total count of all locations of business for the Company"""


class Company(BaseModel):
    company_uid: str
    """Unique alphanumeric Grata ID for the company (case-sensitive)."""

    name: str
    """Name of the company."""

    business_models: Optional[
        List[
            Literal[
                "Software",
                "Software Enabled",
                "Services",
                "Retailer",
                "Manufacturer",
                "Distributor",
                "Producer",
                "Hardware",
                "Content & Publishing",
                "Investment Banks & Business Brokers",
                "Education",
                "Directory",
                "Job Site",
                "Staff & Recruiting",
                "Private Equity & Venture Capital",
                "Private Schools",
                "Hospitals & Medical Centers",
                "Colleges & Universities",
                "Government",
                "US Federal Agencies",
                "Nonprofit & Associations",
                "Religious Institutions",
                "Marketplace",
            ]
        ]
    ] = None
    """Method of product or service delivery."""

    classifications: Optional[Classifications] = None
    """Classifications for the company."""

    conferences: Optional[Conferences] = None
    """Conferences the company has or will attend."""

    contacts: Optional[Contacts] = None
    """Contacts for the company."""

    description: Optional[str] = None
    """Description of the company."""

    domain: Optional[str] = None
    """Domain of the company."""

    domains: Optional[List[Domain]] = None
    """Associated domains for the company.

    Includes foreign domains, secondary domains, and redirects.
    """

    employee_location_breakdown: Optional[List[EmployeeLocationBreakdown]] = None
    """Location breakdown of the employees by country"""

    employees_growth: Optional[EmployeesGrowth] = None
    """Employee growth rate as a percentage."""

    employees_on_professional_networks: Optional[int] = None
    """The number of employees on professional networks."""

    end_customer: Optional[
        List[
            Literal[
                "B2B",
                "B2C",
                "Consumer Products & Retail",
                "Media",
                "Finance",
                "Agriculture",
                "Healthcare",
                "Professional Services",
                "Transportation",
                "Hospitality & Leisure",
                "Government",
                "Education",
                "Electronics",
                "Information Technology",
                "Industrials",
                "Commercial & Residential Services",
            ]
        ]
    ] = None
    """End vertical that the company sells to."""

    entity_type: Optional[
        Literal[
            "Event",
            "Private",
            "Public",
            "Government",
            "Industry Organization",
            "Non-Profit",
            "Private Equity",
            "Subsidiary",
        ]
    ] = None
    """The company's entity classification."""

    funding_rounds_count: Optional[int] = None
    """Rounds of equity funding the company has received."""

    funding_stage: Optional[
        Literal[
            "Early Stage Funding",
            "Late Stage Funding",
            "Pre-IPO Funding",
            "Private Equity Backed",
            "Other Funding",
            "Public",
        ]
    ] = None
    """Stage of funding a company has received."""

    grata_employee_estimates: Optional[int] = None
    """Grata's employee estimates"""

    headquarters: Optional[str] = None
    """City and region of headquarters."""

    investors: Optional[Investors] = None
    """Investors of the company."""

    is_active: Optional[str] = None
    """Indicates if this company is active in platform."""

    keywords: Optional[List[str]] = None
    """Top 10 most relevant keywords that relate to the company's operations."""

    latest_funding_amount: Optional[float] = None
    """The last funding amount received."""

    latest_funding_date: Optional[date] = None
    """The date of the last funding round."""

    latest_funding_round: Optional[str] = None
    """The type of the last funding round."""

    locations: Optional[Locations] = None
    """Locations of business."""

    organization_type: Optional[
        Literal[
            "Company",
            "Independent",
            "Private Equity",
            "Public Subsidiary",
            "Private Subsidiary",
            "Private Equity Add-On",
            "Private Equity Platform",
        ]
    ] = None
    """The type of organization."""

    owner: Optional[Owner] = None
    """Owner information."""

    ownership_status: Optional[
        Literal[
            "Bootstrapped",
            "Investor Backed",
            "Public Subsidiary",
            "Public",
            "Private Subsidiary",
            "Private Equity Add-On",
            "Private Equity",
        ]
    ] = None
    """Current ownership status of the company."""

    primary_email: Optional[str] = None
    """Primary company email from home page or contact section of the website."""

    primary_phone: Optional[str] = None
    """Primary company phone number from home page or contact section of the website."""

    revenue_estimates: Optional[float] = None
    """Grata's revenue estimate"""

    social_crunchbase: Optional[str] = None
    """Link to the company's Crunchbase page."""

    social_facebook: Optional[str] = None
    """Link to the company's Facebook page."""

    social_instagram: Optional[str] = None
    """Link to the company's Instagram page."""

    social_linkedin: Optional[str] = None
    """Link to the company's LinkedIn page."""

    social_twitter: Optional[str] = None
    """Link to the company's Twitter page."""

    total_funding: Optional[float] = None
    """The total funding amount received."""

    ultimate_entity_type: Optional[
        Literal[
            "Event",
            "Public",
            "Private",
            "Government",
            "Industry Organization",
            "Non-Profit",
            "Private Equity",
            "Subsidiary",
        ]
    ] = None
    """Ultimate owner company type."""

    ultimate_owner: Optional[Owner] = None
    """Owner information."""

    url: Optional[str] = None
    """URL to the company's Grata profile."""

    year_founded: Optional[int] = None
    """Founding year of the company."""
