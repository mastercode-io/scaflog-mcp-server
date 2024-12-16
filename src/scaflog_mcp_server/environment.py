from enum import Enum
from typing import Optional
import os
from dotenv import load_dotenv

class Environment(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"

class EnvironmentManager:
    _instance: Optional['EnvironmentManager'] = None
    _current_env: Environment

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Default to development if not specified
            env_name = os.getenv("APP_ENV", "development").lower()
            cls._instance._current_env = Environment(env_name)
        return cls._instance

    @classmethod
    def get_environment(cls) -> Environment:
        return cls().current_env

    @classmethod
    def is_development(cls) -> bool:
        return cls().current_env == Environment.DEVELOPMENT

    @classmethod
    def is_production(cls) -> bool:
        return cls().current_env == Environment.PRODUCTION

    @classmethod
    def is_testing(cls) -> bool:
        return cls().current_env == Environment.TESTING

    @property
    def current_env(self) -> Environment:
        return self._current_env

    @classmethod
    def init(cls, env: str):
        """Explicitly set the environment (useful for testing)"""
        instance = cls()
        instance._current_env = Environment(env.lower()) 