from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.agent.orchestrator import agent
from app.security.auth import get_current_user


router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    question: str
    context: dict = Field(default_factory=dict)


@router.post("")
async def ask(
    request: AskRequest,
    user_id: str = Depends(get_current_user),
):
    return await agent.run(
        user_input=request.question,
        context={
            **request.context,
            "input_type": "follow_up",
            "user_id": user_id,
        },
    )
