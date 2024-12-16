# src_scaflog_zoho_mcp_server/resource_manager.py

from typing import Optional, Dict, List
from pydantic import BaseModel
from scaflog_mcp_server.models import FieldConfig, FormConfig, ReportConfig, ResourceCategory
from scaflog_mcp_server.scaflog_resources import ZOHO_RESOURCES


class ResourceManager:
    """Manages access to Zoho Creator resources."""
    
    def __init__(self):
        self.resources = ZOHO_RESOURCES


    def get_category(self, category_id: str) -> Optional[ResourceCategory]:
        """Get a resource category by ID."""
        return self.resources.get(category_id)


    def get_form(self, category_id: str, form_id: str) -> Optional[FormConfig]:
        """Get a form configuration by category and form ID."""
        category = self.get_category(category_id)
        if category:
            return category.forms.get(form_id)
        return None


    def get_report(self, category_id: str, report_id: str) -> Optional[ReportConfig]:
        """Get a report configuration by category and report ID."""
        category = self.get_category(category_id)
        if category:
            return category.reports.get(report_id)
        return None


    def list_categories(self) -> List[Dict]:
        """List all available resource categories."""
        return [
            {
                "id": cat_id,
                "display_name": cat.display_name,
                "description": cat.description
            }
            for cat_id, cat in self.resources.items()
        ]


    def list_forms(self, category_id: str) -> List[Dict]:
        """List all forms in a category."""
        category = self.get_category(category_id)
        if not category:
            return []
        
        return [
            {
                "id": form_id,
                "display_name": form.display_name,
                "description": form.description
            }
            for form_id, form in category.forms.items()
        ]


    def list_reports(self, category_id: str) -> List[Dict]:
        """List all reports in a category."""
        category = self.get_category(category_id)
        if not category:
            return []
        
        return [
            {
                "id": report_id,
                "display_name": report.display_name,
                "description": report.description
            }
            for report_id, report in category.reports.items()
        ]
    