from fastapi import FastAPI, Depends, status

from routes import configure_routes
from error_handlers import configure_error_handlers
from services import verify_token, verify_key

app = FastAPI()
# NOTE: This will enforce that every single request need token and key.
# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

@app.get("/")
async def health():
    return {"status": status.HTTP_200_OK}

configure_error_handlers(app)
configure_routes(app)
