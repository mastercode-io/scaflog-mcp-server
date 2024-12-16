# src_scaflog_zoho_mcp_server/server.py

from fastmcp import FastMCP
from scaflog_mcp_server.resource_manager import ResourceManager
import json
from scaflog_mcp_server import logger, setup_logger
from scaflog_mcp_server.environment import EnvironmentManager


# Pre-declare handlers to satisfy linter
get_job = None
get_task_names = None
validate_job = None
collect_phase_info = None
validate_phase_data = None


class ScaflogMCPServer:

    def __init__(self):
        # Add unconditional logging before environment check
        log = setup_logger("scaflog_mcp_server.server")
        log.info("Initializing ScaflogMCPServer")  # This should always appear

        self.mcp = FastMCP("Scaflog")
        self.resource_manager = ResourceManager()

        logger.info(f"Environment: {EnvironmentManager.get_environment()}")
        if EnvironmentManager.is_development():
            logger.info("Running in development mode")

        log.info("Registering handlers...")
        self.register_handlers()
        log.info("Handlers registered")


    def register_handlers(self):
        global get_job, get_task_names, validate_job, collect_phase_info, validate_phase_data

        @self.mcp.resource("zoho://jobs/get/{job_number}")
        def get_job(job_number: str) -> str:
            result = self.resource_manager.validate_job("COMPANY_ID", job_number)
            return json.dumps(result)

        @self.mcp.resource("zoho://tasks/names")
        def get_task_names() -> str:
            result = self.resource_manager.get_task_names()
            return json.dumps(result)

        # Tool for job validation
        @self.mcp.tool()
        def validate_job(company_id: str, job_number: str) -> str:
            """Validate job and return record ID if valid."""
            try:
                result = self.resource_manager.validate_job(company_id, job_number)
                return json.dumps({
                    "success": True,
                    "data": result
                })
            except ValueError as e:
                return json.dumps({
                    "success": False,
                    "error": str(e)
                })

        # Prompts for phase creation
        @self.mcp.prompt()
        def collect_phase_info() -> str:
            """Prompt template for collecting phase information."""
            return """Please collect the following required information for the new phase:
            1. Phase Name (text)
            2. Phase Type (must be one of: Construction, Design, Planning)
            3. Start Date (format: YYYY-MM-DD)

            Ask for each piece of information separately and validate the response.
            For Phase Type, only accept the exact values listed.
            For Start Date, ensure it's a valid date in the correct format.

            After collecting all information, validate the complete dataset.
            """

        @self.mcp.prompt()
        def validate_phase_data() -> str:
            """Prompt template for validating collected phase data."""
            return """Please validate the following phase data:
            {phase_data}

            Check:
            1. All required fields are present
            2. Phase Type is valid
            3. Start Date is in correct format
            4. No invalid characters in Phase Name

            Return the validated data in JSON format or list any validation errors.
            """


# Create server instance
server = ScaflogMCPServer()
# Export mcp instance for FastMCP to use
mcp = server.mcp
