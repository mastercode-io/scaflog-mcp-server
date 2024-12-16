# src_scaflog_zoho_mcp_server/resource_config.py

from typing import Dict, List, Optional
from pydantic import BaseModel

class FieldConfig(BaseModel):
    """Configuration for a whitelisted field."""
    display_name: str
    description: Optional[str] = None
    required: bool = False

class FormConfig(BaseModel):
    """Configuration for a whitelisted form."""
    app_name: str
    link_name: str
    display_name: str
    description: Optional[str] = None
    fields: Dict[str, FieldConfig]

class ReportConfig(BaseModel):
    """Configuration for a whitelisted report."""
    app_name: str
    link_name: str
    display_name: str
    description: Optional[str] = None
    fields: Dict[str, FieldConfig]
