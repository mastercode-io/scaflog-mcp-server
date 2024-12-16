# src/scaflog_mcp_server/logger.py
# This is the logger for the MCP server
# It is used to log messages to the console and to a file


import logging
import sys
from pathlib import Path
from .environment import EnvironmentManager


def setup_logger(name: str = None) -> logging.Logger:
    logger = logging.getLogger(name or __name__)
    
    if not logger.handlers:  # Avoid adding handlers multiple times
        # Get project root directory (2 levels up from logger.py)
        project_root = Path(__file__).parent.parent.parent
        
        # Create logs directory if it doesn't exist
        log_dir = project_root / "logs"
        log_dir.mkdir(exist_ok=True)
        
        # Configure file handler to append to the file
        file_handler = logging.FileHandler(log_dir / "app.log", mode='a')
        console_handler = logging.StreamHandler(sys.stdout)
        
        # Use the same detailed formatting for both environments
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        if EnvironmentManager.is_development():
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        
        # Apply formatter to both handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add both handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Log the project root and log file location at startup
        logger.info(f"Project root: {project_root}")
        logger.info(f"Log file: {log_dir / 'app.log'}")
    
    return logger