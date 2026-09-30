from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.agent.orchestrator import agent

router = APIRouter(prefix="/search", tags=["search"])


class SearchRequest(BaseModel):
    query: str
    context: dict = Field(default_factory=dict)


@router.post("")
async def search(request: SearchRequest):
    result = await agent.run(
        user_input=request.query,
        context={
            **request.context,
            "input_type": "search",
        },
    )

    return result
