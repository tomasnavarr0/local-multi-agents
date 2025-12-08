from agent_framework import ChatAgent
from app.utils.clients import BaseClient
from typing import Any

class AgentGenerator:

    def generate_agent(*, client: BaseClient, instruction: str, name: str, **kwargs: Any) -> ChatAgent:
        return ChatAgent(client=client.generate_chat_client(),
                         instructions=instruction,
                         name=name,
                         **kwargs
                         )