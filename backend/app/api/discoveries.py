from fastapi import APIRouter

from app.discoveries.service import discoveries_service

router = APIRouter(prefix="/discoveries", tags=["discoveries"])


@router.get("")
async def list_discoveries(user_id: str):
    return await discoveries_service.list(user_id)


@router.get("/{discovery_id}")
async def get_discovery(discovery_id: str, user_id: str):
    return await discoveries_service.get(user_id, discovery_id)
