from fastapi import FastAPI

from routers.app_health_get import app_health_get
from routers.app_health_put import app_health_put
from routers.app_health_post import app_health_post
from routers.app_extra_router import app_extra_router
from routers.app_form_data import app_form_data_router
from routers.app_error_handling import app_error_handling_router

def configure_routes(app: FastAPI):
    app.include_router(app_error_handling_router, prefix="/error-handling", tags=["Error Handling"])    
    # app.include_router(app_form_data_router, prefix="/form-data", tags=["Form Data"])
    # app.include_router(app_extra_router, prefix="/extra", tags=["Extra"])
    # app.include_router(app_health_get, prefix="/health-get", tags=["Health GET"])
    # app.include_router(app_health_put, prefix="/health-put", tags=["Health PUT"])
    # app.include_router(app_health_post, prefix="/health-post", tags=["Health POST"])