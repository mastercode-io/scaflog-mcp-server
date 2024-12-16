# src/scaflog_mcp_server/config.py

import json
from pathlib import Path
from typing import Dict, Any, Optional
from scaflog_mcp_server.models import ResourceConfig, FormConfig, FieldConfig


class ConfigLoader:
    def __init__(self, config_dir: Optional[Path] = None):
        self.config_dir = config_dir or Path(__file__).parent.parent.parent / "config"
        self.resources: Dict[str, ResourceConfig] = {}


    def load_resources(self) -> None:
        """Load resource configurations."""
        resource_file = self.config_dir / "resources" / "core.json"
        
        if not resource_file.exists():
            raise FileNotFoundError(f"Resource config not found: {resource_file}")

        with open(resource_file) as f:
            data = json.load(f)
            
        self.resources = {
            key: ResourceConfig(**config)
            for key, config in data.items()
        }


    def get_resource(self, resource_id: str) -> Optional[ResourceConfig]:
        """Get resource configuration by ID."""
        return self.resources.get(resource_id)
    