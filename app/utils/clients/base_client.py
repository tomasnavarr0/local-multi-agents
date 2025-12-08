from abc import ABC, abstractmethod
from agent_framework.openai import OpenAIChatClient

class BaseClient(ABC):

    @staticmethod
    @abstractmethod
    def generate_chat_client() -> OpenAIChatClient:
        pass