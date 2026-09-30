import os

from openai import AsyncOpenAI


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


def get_openai_client() -> AsyncOpenAI:
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not configured."
        )

    return AsyncOpenAI(
        api_key=OPENAI_API_KEY,
    )
