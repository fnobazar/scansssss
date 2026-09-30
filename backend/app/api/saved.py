from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.saved.service import saved_service
from app.security.auth import get_current_user


router = APIRouter(prefix="/saved", tags=["saved"])


class SaveRequest(BaseModel):
    discovery_id: str


@router.get("")
async def list_saved(
    user_id: str = Depends(get_current_user),
):
    return await saved_service.list(user_id)


@router.post("")
async def save_item(
    request: SaveRequest,
    user_id: str = Depends(get_current_user),
):
    return await saved_service.save(
        user_id=user_id,
        discovery_id=request.discovery_id,
    )


@router.delete("/{discovery_id}")
async def delete_saved(
    discovery_id: str,
    user_id: str = Depends(get_current_user),
):
    return await saved_service.delete(
        user_id=user_id,
        discovery_id=discovery_id,
    )
