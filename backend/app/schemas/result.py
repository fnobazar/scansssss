from typing import Any, Literal

from pydantic import BaseModel, Field


class ResultSection(BaseModel):
    type: str
    data: dict[str, Any] = Field(default_factory=dict)


class DynamicResult(BaseModel):
    type: Literal[
        "product",
        "place",
        "object",
        "person",
        "document",
        "plant",
        "animal",
        "palm",
        "general",
    ] = "general"

    title: str
    description: str = ""
    confidence: float | None = None
    sections: list[ResultSection] = Field(default_factory=list)
    actions: list[str] = Field(default_factory=list)
    sources: list[dict[str, Any]] = Field(default_factory=list)
