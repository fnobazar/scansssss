from typing import Any


class ResearchService:
    async def search(self, query: str) -> dict[str, Any]:
        return {
            "query": query,
            "status": "pending",
            "results": [],
            "message": "Web research provider will be connected here.",
        }


research_service = ResearchService()
