import os

from fastapi import Header, HTTPException
from jose import JWTError, jwt


SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET", "")


async def get_current_user(
    authorization: str | None = Header(default=None),
) -> str:
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authentication required",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication format",
        )

    token = authorization.replace("Bearer ", "", 1).strip()

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token",
        )

    if not SUPABASE_JWT_SECRET:
        raise HTTPException(
            status_code=500,
            detail="Supabase JWT secret is not configured",
        )

    try:
        payload = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            options={"verify_aud": False},
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired authentication token",
        )

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="User ID missing from token",
        )

    return user_id
