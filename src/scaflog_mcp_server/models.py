# src/scaflog_mcp_server/models.py

from typing import Optional, Dict
from pydantic import BaseModel


class FieldConfig(BaseModel):
    """Configuration for a whitelisted field."""
    display_name: str
    description: Optional[str] = None
    required: bool = False


class FormConfig(BaseModel):
    """Configuration for a whitelisted form."""
    link_name: str
    display_name: str
    description: Optional[str] = None
    fields: Dict[str, FieldConfig]


class ReportConfig(BaseModel):
    """Configuration for a whitelisted report."""
    link_name: str
    display_name: str
    description: Optional[str] = None
    fields: Dict[str, FieldConfig]


class ResourceConfig(BaseModel):
    """Resource category configuration."""
    app_name: str
    display_name: str
    description: str
    forms: Dict[str, FormConfig]
    reports: Dict[str, ReportConfig]


class ResourceCategory(BaseModel):
    """Group of related forms and reports."""
    display_name: str
    description: str
    forms: Dict[str, FormConfig]
    reports: Dict[str, ReportConfig]
    