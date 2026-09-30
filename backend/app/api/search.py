from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.agent.orchestrator import agent
from app.security.auth import get_current_user


router = APIRouter(prefix="/search", tags=["search"])


class SearchRequest(BaseModel):
    query: str
    context: dict = Field(default_factory=dict)


@router.post("")
async def search(
    request: SearchRequest,
    user_id: str = Depends(get_current_user),
):
    return await agent.run(
        user_input=request.query,
        context={
            **request.context,
            "input_type": "search",
            "user_id": user_id,
        },
    )
