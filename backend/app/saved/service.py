from typing import Any

from app.database.repository import database_repository


class SavedService:

    async def list(self, user_id: str) -> dict[str, Any]:
        items = await database_repository.get_saved(user_id)

        return {
            "user_id": user_id,
            "items": items,
        }

    async def save(
        self,
        user_id: str,
        discovery_id: str,
    ) -> dict[str, Any]:
        client = database_repository.client

        response = (
            client
            .table("saved_items")
            .insert({
                "user_id": user_id,
                "discovery_id": discovery_id,
            })
            .execute()
        )

        return {
            "user_id": user_id,
            "discovery_id": discovery_id,
            "status": "saved",
            "item": response.data[0] if response.data else None,
        }

    async def delete(
        self,
        user_id: str,
        discovery_id: str,
    ) -> dict[str, Any]:
        client = database_repository.client

        (
            client
            .table("saved_items")
            .delete()
            .eq("user_id", user_id)
            .eq("discovery_id", discovery_id)
            .execute()
        )

        return {
            "user_id": user_id,
            "discovery_id": discovery_id,
            "status": "deleted",
        }


saved_service = SavedService()
