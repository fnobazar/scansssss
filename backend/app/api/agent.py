from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.orchestrator import agent

router = APIRouter(prefix="/agent", tags=["agent"])


class AgentRequest(BaseModel):
    user_input: str
    context: dict = {}


@router.post("/run")
async def run_agent(request: AgentRequest):
    return await agent.run(
        user_input=request.user_input,
        context=request.context,
    )
