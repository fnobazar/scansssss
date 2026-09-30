import os

from supabase import create_client, Client


SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_PUBLISHABLE_KEY = os.getenv(
    "SUPABASE_PUBLISHABLE_KEY",
    "",
)


def get_supabase_client() -> Client:
    if not SUPABASE_URL or not SUPABASE_PUBLISHABLE_KEY:
        raise RuntimeError(
            "Supabase configuration is missing."
        )

    return create_client(
        SUPABASE_URL,
        SUPABASE_PUBLISHABLE_KEY,
    )
