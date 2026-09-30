from typing import Any

from app.database.client import get_supabase_client


class DatabaseRepository:

    def __init__(self) -> None:
        self.client = get_supabase_client()

    async def get_discoveries(
        self,
        user_id: str,
    ) -> list[dict[str, Any]]:
        response = (
            self.client
            .table("discoveries")
            .select("*")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )

        return response.data or []

    async def get_saved(
        self,
        user_id: str,
    ) -> list[dict[str, Any]]:
        response = (
            self.client
            .table("saved_items")
            .select("*")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )

        return response.data or []


database_repository = DatabaseRepository()
