# src/scaflog_mcp_server/resource_manager.py

from typing import Optional, Dict, Any
from scaflog_mcp_server.config import ConfigLoader
from scaflog_mcp_server.zoho_client import ZohoClient  # We'll create this later
from scaflog_mcp_server.environment import EnvironmentManager
from scaflog_mcp_server import logger


class ResourceManager:
    def __init__(self):
        self.config = ConfigLoader()
        self.config.load_resources()
        self.zoho_client = ZohoClient(self.config)


    def validate_job(self, company_id: str, job_number: str) -> Dict[str, Any]:
        """Validate job exists and get its record ID."""
        if EnvironmentManager.is_development():
            logger.info(f"Mocking job validation for {company_id}/{job_number}")
            return {
                "record_id": "mock_id",
                "job_number": job_number,
                "status": "Active"
            }
        job = self.zoho_client.get_job(company_id, job_number)
        
        if not job:
            raise ValueError(f"Job {job_number} not found")
            
        if job["Status"] not in ["Active", "On Hold"]:
            raise ValueError(f"Job {job_number} is not in valid state for adding phases")
            
        return {
            "record_id": job["Record_ID"],
            "job_number": job["Job_Number"],
            "status": job["Status"]
        }


    def get_phase_requirements(self) -> Dict[str, Any]:
        """Get phase creation requirements."""
        phase_config = self.config.get_resource("phases")
        if not phase_config:
            raise ValueError("Phase configuration not found")
            
        return phase_config.forms["Requirements"].dict()


    def get_task_names(self) -> Dict[str, Any]:
        """Get available task names."""
        return self.zoho_client.get_task_names()
    