from typing import Any


class AgentOrchestrator:
    def __init__(self) -> None:
        self.name = "Sca-N Main Agent"

    async def run(self, user_input: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        return {
            "type": "general",
            "title": "Sca-N",
            "description": f"Received: {user_input}",
            "sections": [],
            "actions": ["ask_more", "save"],
            "sources": [],
        }


agent = AgentOrchestrator()
