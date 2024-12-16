# src_scaflog_zoho_mcp_server/server.py

from fastmcp import FastMCP
from scaflog_mcp_server.resource_manager import ResourceManager
import json


mcp = FastMCP("Scaflog")
resource_manager = ResourceManager()


@mcp.resource("zoho://categories")
def list_categories() -> str:
    """List all resource categories."""
    categories = resource_manager.list_categories()
    return json.dumps(categories)


@mcp.resource("zoho://categories/{category_id}")
def get_category(category_id: str) -> str:
    """Get a specific category by ID."""
    category = resource_manager.get_category(category_id)
    if category:
        return json.dumps({
            "category": category_id,
            "display_name": category.display_name,
            "description": category.description,
            "forms": resource_manager.list_forms(category_id),
            "reports": resource_manager.list_reports(category_id)
        }, indent=2)
    return json.dumps({"error": f"Category {category_id} not found"}, indent=2)


@mcp.resource("zoho://{category}/forms")
def list_category_forms(category: str) -> str:
    """List all forms in a category."""
    forms = resource_manager.list_forms(category)
    return json.dumps(forms)


@mcp.resource("zoho://{category}/reports")
def list_category_reports(category: str) -> str:
    """List all reports in a category."""
    reports = resource_manager.list_reports(category)
    return json.dumps(reports)


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
