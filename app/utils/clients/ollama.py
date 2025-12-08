from agent_framework.openai import OpenAIChatClient

from .base_client import BaseClient


class OllamaClient(BaseClient):

    @staticmethod
    def generate_chat_client() -> OpenAIChatClient:
        return OpenAIChatClient(
            api_key="ollama",
            model_id="llama3.2:1b",
            base_url="http://localhost:11434/v1" 
        )

