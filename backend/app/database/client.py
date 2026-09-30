import os

from supabase import Client, create_client


SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_PUBLISHABLE_KEY = os.getenv(
    "SUPABASE_PUBLISHABLE_KEY",
    "",
)


def get_supabase_client(
    access_token: str | None = None,
) -> Client:
    if not SUPABASE_URL or not SUPABASE_PUBLISHABLE_KEY:
        raise RuntimeError(
            "Supabase configuration is missing."
        )

    client = create_client(
        SUPABASE_URL,
        SUPABASE_PUBLISHABLE_KEY,
    )

    if access_token:
        client.postgrest.auth(access_token)

    return client
