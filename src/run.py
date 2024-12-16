# src/run.py
# This is the entry point for the MCP server
# It is used to start the server and log the startup process


import os
import sys
import asyncio
from pathlib import Path


# Early startup logging
startup_log = Path('/tmp/mcp_startup.log')
startup_log.write_text('MCP Server startup attempted\n')

# Add the src directory to Python path
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, src_path)

startup_log.write_text(f'Python path: {sys.path}\n')

from scaflog_mcp_server.server import mcp


async def main():
    startup_log.write_text('Async main started\n')
    try:
        await mcp.run()
    except Exception as e:
        startup_log.write_text(f'Error in main: {str(e)}\n')
        raise


if __name__ == "__main__":
    startup_log.write_text('Main block executed\n')
    asyncio.run(main())
