from fastapi import APIRouter, Depends

from app.discoveries.service import discoveries_service
from app.security.auth import get_current_user


router = APIRouter(prefix="/discoveries", tags=["discoveries"])


@router.get("")
async def list_discoveries(
    user_id: str = Depends(get_current_user),
):
    return await discoveries_service.list(user_id)


@router.get("/{discovery_id}")
async def get_discovery(
    discovery_id: str,
    user_id: str = Depends(get_current_user),
):
    return await discoveries_service.get(
        user_id,
        discovery_id,
    )
