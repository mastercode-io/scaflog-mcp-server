# src_scaflog_zoho_mcp_server/zoho_resources.py

from typing import Dict
from pydantic import BaseModel, Field
from scaflog_mcp_server.models import FormConfig, ReportConfig, FieldConfig


class ResourceCategory(BaseModel):
    """Group of related forms and reports."""
    display_name: str
    description: str
    forms: Dict[str, FormConfig]
    reports: Dict[str, ReportConfig]


ZOHO_RESOURCES = {
    "jobs": ResourceCategory(
        display_name="Jobs",
        description="Job management and tracking",
        forms={
            "Jobs": FormConfig(
                link_name="Jobs",
                display_name="Jobs",
                description="Main job record",
                fields={
                    "Job_Number": FieldConfig(
                        display_name="Job Number",
                        description="Unique job identifier",
                        required=True
                    ),
                    "Job_Name": FieldConfig(
                        display_name="Job Name",
                        description="Name/title of the job",
                        required=True
                    ),
                    "Client": FieldConfig(
                        display_name="Client",
                        description="Associated client",
                        required=True
                    ),
                    "Status": FieldConfig(
                        display_name="Status",
                        description="Current job status"
                    ),
                }
            ),
        },
        reports={
            "All_Jobs": ReportConfig(
                link_name="All_Jobs",
                display_name="All Jobs",
                description="Complete list of jobs with details",
                fields={
                    "Job_Number": FieldConfig(
                        display_name="Job Number",
                        description="Unique job identifier"
                    ),
                    "Job_Name": FieldConfig(
                        display_name="Job Name",
                        description="Name of the job"
                    ),
                    "Client": FieldConfig(
                        display_name="Client",
                        description="Associated client"
                    ),
                    "Status": FieldConfig(
                        display_name="Status",
                        description="Current status"
                    ),
                }
            ),
            "Active_Jobs": ReportConfig(
                link_name="Active_Jobs",
                display_name="Active Jobs",
                description="Currently active jobs",
                fields={
                    "Job_Number": FieldConfig(
                        display_name="Job Number",
                        description="Unique job identifier"
                    ),
                    "Status": FieldConfig(
                        display_name="Status",
                        description="Current status"
                    ),
                }
            ),
        }
    ),

    "phases": ResourceCategory(
        display_name="Phases and Quotes",
        description="Job phases and associated quotes",
        forms={
            "Phases": FormConfig(
                link_name="Phases",
                display_name="Phases",
                description="Job phase information",
                fields={
                    "Phase_Number": FieldConfig(
                        display_name="Phase Number",
                        description="Phase identifier",
                        required=True
                    ),
                    "Job": FieldConfig(
                        display_name="Job",
                        description="Associated job",
                        required=True
                    ),
                    "Status": FieldConfig(
                        display_name="Status",
                        description="Phase status"
                    ),
                }
            ),
            "Quote_Lines": FormConfig(
                link_name="Quote_Lines",
                display_name="Quote Lines",
                description="Individual quote line items",
                fields={
                    "Phase": FieldConfig(
                        display_name="Phase",
                        description="Associated phase",
                        required=True
                    ),
                    "Product": FieldConfig(
                        display_name="Product",
                        description="Quoted product",
                        required=True
                    ),
                    "Quantity": FieldConfig(
                        display_name="Quantity",
                        description="Quote quantity",
                        required=True
                    ),
                }
            ),
        },
        reports={
            "Phase_Quotes": ReportConfig(
                link_name="Phase_Quotes",
                display_name="Phase Quotes",
                description="Quotes by phase",
                fields={
                    "Phase": FieldConfig(
                        display_name="Phase",
                        description="Job phase"
                    ),
                    "Total_Amount": FieldConfig(
                        display_name="Total Amount",
                        description="Total quote amount"
                    ),
                }
            ),
        }
    ),
}

# Add more categories following the same pattern...