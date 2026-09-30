from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.agent.orchestrator import agent

router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    question: str
    context: dict = Field(default_factory=dict)


@router.post("")
async def ask(request: AskRequest):
    result = await agent.run(
        user_input=request.question,
        context={
            **request.context,
            "input_type": "follow_up",
        },
    )

    return result
