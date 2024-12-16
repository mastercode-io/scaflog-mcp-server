# src/scaflog_mcp_server/zoho_client.py

from typing import Dict, Any
from scaflog_mcp_server.zoho_auth import ZohoCreatorConfig, API_BASE_URL
import httpx
from scaflog_mcp_server import logger
from scaflog_mcp_server.environment import EnvironmentManager
from pathlib import Path
import json


class ZohoClient:


    def __init__(self, config: ZohoCreatorConfig):
        self.config = config
        if EnvironmentManager.is_development():
            logger.debug("Initializing ZohoClient in development mode")



    def get_job(self, company_id: str, job_number: str) -> Dict[str, Any]:
        """Get job details."""
        if EnvironmentManager.is_development():
            logger.info(f"Mocking job details for company {company_id} and job {job_number}")
            return {
                "Record_ID": "123",
                "Job_Number": "123",
                "Status": "Active"
            }
        url = f"{API_BASE_URL}/jobs/{company_id}/{job_number}"
        headers = {"Authorization": f"Zoho-oauthtoken {self.config.access_token}"}
        response = httpx.get(url, headers=headers)
        return response.json()
    

    def get_task_names(self) -> Dict[str, Any]:
        """Get list of available task names."""
        if EnvironmentManager.is_development():
            logger.info(f"Loading task names from config file")
        
        try:
            config_path = Path(__file__).parent.parent.parent / "config/resources" / "task_names.json"
            with open(config_path) as f:
                task_names_list = json.load(f)
            return {"task_names": task_names_list}
        except FileNotFoundError:
            logger.info("Task names configuration file not found")
            return {"task_names": []}
        except json.JSONDecodeError:
            logger.info("Invalid JSON in task names configuration file")
            return {"task_names": []}
