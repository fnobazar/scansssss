from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.agent.orchestrator import agent

router = APIRouter(prefix="/scan", tags=["scan"])


class ScanRequest(BaseModel):
    image_url: str
    context: dict = Field(default_factory=dict)


@router.post("")
async def scan(request: ScanRequest):
    result = await agent.run(
        user_input="Identify and understand this scanned image.",
        context={
            **request.context,
            "image_url": request.image_url,
            "input_type": "image",
        },
    )

    return result
