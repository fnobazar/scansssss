from app.ai.client import get_openai_client
from app.agent.result_builder import result_builder
def detect_intent(
    self,
    context: dict[str, Any],
) -> str:
    input_type = context.get("input_type", "general")

    if input_type == "image":
        return "scan"

    if input_type == "search":
        return "search"

    if input_type == "follow_up":
        return "follow_up"

    if input_type == "product":
        return "product"

    if input_type == "place":
        return "place"

    if input_type == "document":
        return "document"

    if input_type == "palm":
        return "palm"

    return "general"
