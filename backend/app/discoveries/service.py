from typing import Any

from app.database.repository import database_repository


class DiscoveriesService:

    async def list(self, user_id: str) -> dict[str, Any]:
        discoveries = await database_repository.get_discoveries(
            user_id
        )

        return {
            "user_id": user_id,
            "discoveries": discoveries,
        }

    async def get(
        self,
        user_id: str,
        discovery_id: str,
    ) -> dict[str, Any]:

        discoveries = await database_repository.get_discoveries(
            user_id
        )

        discovery = next(
            (
                item
                for item in discoveries
                if str(item.get("id")) == str(discovery_id)
            ),
            None,
        )

        return {
            "user_id": user_id,
            "discovery_id": discovery_id,
            "discovery": discovery,
        }


discoveries_service = DiscoveriesService()
    )
