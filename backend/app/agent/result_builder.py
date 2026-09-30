from typing import Any


class ResultBuilder:

    def build(
        self,
        *,
        title: str,
        description: str,
        result_type: str = "general",
        confidence: float | None = None,
        sections: list[dict[str, Any]] | None = None,
        actions: list[str] | None = None,
        sources: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:

        return {
            "type": result_type,
            "title": title,
            "description": description,
            "confidence": confidence,
            "sections": sections or [],
            "actions": actions or [
                "ask_more",
                "save",
            ],
            "sources": sources or [],
        }


result_builder = ResultBuilder()
