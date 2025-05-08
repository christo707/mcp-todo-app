import json
import os
from typing import Any, Optional

import dotenv

OLLAMA_MODEL_NAME = "qwen2.5"
OLLAMA_BASE_URL = "http://localhost:11434"


class Configuration:
    """Manages configuration and environment variables for the MCP client."""

    def __init__(self) -> None:
        """Initialize configuration with environment variables."""
        self.load_env()

        self._ollama_model_name = OLLAMA_MODEL_NAME
        self._ollama_base_url = OLLAMA_BASE_URL

    @staticmethod
    def load_env() -> None:
        """Load environment variables from .env file."""
        dotenv.load_dotenv()

    @staticmethod
    def load_config(file_path: str) -> dict[str, Any]:
        """Load server configuration from JSON file.

        Args:
            file_path: Path to the JSON configuration file.

        Returns:
            Dict containing server configuration.

        Raises:
            FileNotFoundError: If configuration file doesn't exist.
            JSONDecodeError: If configuration file is invalid JSON.
        """
        with open(file_path, "r") as f:
            return json.load(f)

    @property
    def ollama_model_name(self) -> str:
        """Get the Ollama model name.

        Returns:
            The model name as a string.
        """
        if not self._ollama_model_name:
            raise ValueError("OLLAMA_MODEL_NAME not found in environment variables")
        return self._ollama_model_name

    @property
    def ollama_base_url(self) -> Optional[str]:
        """Get the Ollama base URL.

        Returns:
            The base URL as a string.
        """
        if not self._ollama_base_url:
            raise ValueError("OLLAMA_BASE_URL not found in environment variables")
        return self._ollama_base_url