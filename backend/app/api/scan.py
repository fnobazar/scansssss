from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.agent.orchestrator import agent
from app.security.auth import get_current_user


router = APIRouter(prefix="/scan", tags=["scan"])


class ScanRequest(BaseModel):
    image_url: str
    context: dict = Field(default_factory=dict)


@router.post("")
async def scan(
    request: ScanRequest,
    user_id: str = Depends(get_current_user),
):
    result = await agent.run(
        user_input="Identify and understand this scanned image.",
        context={
            **request.context,
            "image_url": request.image_url,
            "input_type": "image",
            "user_id": user_id,
        },
    )
    return result
