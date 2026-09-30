from typing import Any

from app.ai.client import get_openai_client


class AgentOrchestrator:

    def __init__(self) -> None:
        self.name = "Sca-N Main Agent"

    def detect_intent(
        self,
        context: dict[str, Any],
    ) -> str:
        input_type = context.get("input_type", "general")

        if input_type == "image":
            return "scan"

        if input_type == "search":
            return "search"

        if input_type == "follow_up":
            return "follow_up"

        return "general"

    async def run(
        self,
        user_input: str,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        context = context or {}
        intent = self.detect_intent(context)

        client = get_openai_client()

        response = await client.responses.create(
            model="gpt-5-mini",
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are Sca-N, an AI understanding engine. "
                        "Understand the user's request and provide "
                        "clear, factual and useful information. "
                        "The request intent is: "
                        f"{intent}."
                    ),
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )

        return {
            "type": "general",
            "title": "Sca-N",
            "description": response.output_text,
            "confidence": None,
            "intent": intent,
            "sections": [],
            "actions": ["ask_more", "save"],
            "sources": [],
            "context": context,
        }


agent = AgentOrchestrator()
