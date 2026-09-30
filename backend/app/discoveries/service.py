from typing import Any


class DiscoveriesService:
    async def list(self, user_id: str) -> dict[str, Any]:
        return {
            "user_id": user_id,
            "discoveries": [],
        }

    async def get(self, user_id: str, discovery_id: str) -> dict[str, Any]:
        return {
            "user_id": user_id,
            "discovery_id": discovery_id,
            "discovery": None,
        }


discoveries_service = DiscoveriesService()
