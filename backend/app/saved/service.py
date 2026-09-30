from typing import Any


class SavedService:
    async def list(self, user_id: str) -> dict[str, Any]:
        return {
            "user_id": user_id,
            "items": [],
        }

    async def save(
        self,
        user_id: str,
        discovery_id: str,
    ) -> dict[str, Any]:
        return {
            "user_id": user_id,
            "discovery_id": discovery_id,
            "status": "saved",
        }

    async def delete(
        self,
        user_id: str,
        discovery_id: str,
    ) -> dict[str, Any]:
        return {
            "user_id": user_id,
            "discovery_id": discovery_id,
            "status": "deleted",
        }


saved_service = SavedService()
