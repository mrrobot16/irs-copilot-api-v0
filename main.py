from fastapi import FastAPI, Depends, status
from fastapi.staticfiles import StaticFiles

from routes import configure_routes
from routes.auth import configure_auth_routes
from error_handlers import configure_error_handlers
from middleware import configure_middleware
from metadata import metadata
from services import verify_token, verify_key

app = FastAPI(
    title = metadata["title"],
    description = metadata["description"],
    summary = metadata["summary"],
    version = metadata["version"],
    terms_of_service = metadata["terms_of_service"],
    contact = metadata["contact"],
    license_info = metadata["license_info"],
    openapi_tags = metadata["tags"],
    openapi_url = metadata["openapi_url"],
    dependencies=[Depends(verify_token), Depends(verify_key)], # NOTE: This will enforce that every single request need token and key.
    docs_url="/docs", 
    redoc_url="/documentation"
)

@app.get("/")
async def health():
    return {"status": status.HTTP_200_OK}

configure_error_handlers(app)
configure_middleware(app)
configure_auth_routes(app)
configure_routes(app)
