from fastapi import Header, HTTPException


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

    # Real Supabase JWT verification will be connected in Step 47.
    return token
