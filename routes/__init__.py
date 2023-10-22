from fastapi import FastAPI
from routers.app_health_get import app_health_get
from routers.app_health_put import app_health_put
from routers.app_health_post import app_health_post

def configure_routes(app: FastAPI):
    app.include_router(app_health_get, prefix="/health-get", tags=["Health GET"])
    app.include_router(app_health_put, prefix="/health-put", tags=["Health PUT"])
    app.include_router(app_health_post, prefix="/health-post", tags=["Health POST"])