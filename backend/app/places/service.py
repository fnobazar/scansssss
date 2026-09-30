from typing import Any


class PlaceService:
    async def search(self, query: str) -> dict[str, Any]:
        return {
            "query": query,
            "status": "pending",
            "place": None,
            "location": None,
            "history": [],
            "nearby": [],
            "message": "Maps and place research providers will be connected here.",
        }


place_service = PlaceService()
