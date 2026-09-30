from typing import Any

from app.ai.client import get_openai_client


class AgentOrchestrator:

    def __init__(self) -> None:
        self.name = "Sca-N Main Agent"

    async def run(
        self,
        user_input: str,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        context = context or {}

        client = get_openai_client()

        response = await client.responses.create(
            model="gpt-5-mini",
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are Sca-N, an AI system that helps "
                        "users scan, understand, research, ask "
                        "questions, and save discoveries. "
                        "Return useful, factual information."
                    ),
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )

        answer = response.output_text

        return {
            "type": "general",
            "title": "Sca-N",
            "description": answer,
            "confidence": None,
            "sections": [],
            "actions": ["ask_more", "save"],
            "sources": [],
            "context": context,
        }


agent = AgentOrchestrator()
