from typing import Annotated

from fastapi import Depends, Cookie, HTTPException, Header

async def verify_token(x_token: Annotated[str, Header()] = None):
    pass
    # if x_token != "fake-super-secret-token":
    #     raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()] = None):
    pass
    # if x_key != "fake-super-secret-key":
    #     raise HTTPException(status_code=400, detail="X-Key header invalid")


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q

# async def needy_dependency(fresh_value: Annotated[str, Depends(get_value, use_cache=False)]):
#     return {"fresh_value": fresh_value}

CommonsDep = Annotated[dict, Depends(common_parameters)]

query_or_default = Annotated[str, Depends(query_or_cookie_extractor)]

class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

CommonQPs = Annotated[CommonQueryParams, Depends()]