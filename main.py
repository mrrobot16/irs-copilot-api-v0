from fastapi import FastAPI, Depends, status

from routes import configure_routes
from routes.auth import configure_auth_routes
from error_handlers import configure_error_handlers
from middleware import configure_middleware, origins
# from services import verify_token, verify_key
# NOTE: This will enforce that every single request need token and key.
# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
app = FastAPI()

@app.get("/")
async def health():
    return {"status": status.HTTP_200_OK}

configure_error_handlers(app)
configure_middleware(app)
configure_auth_routes(app)
configure_routes(app)
