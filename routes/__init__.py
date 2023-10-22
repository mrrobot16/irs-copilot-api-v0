from fastapi import FastAPI
from routers.app_health_get import app_health_get
from routers.app_health_put import app_health_put

def configure_routes(app: FastAPI):
    app.include_router(app_health_get, prefix="/health-get", tags=["Health GET"])
    app.include_router(app_health_put, prefix="/health-put", tags=["Health PUT"])
