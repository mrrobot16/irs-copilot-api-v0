from fastapi import FastAPI

from routes import configure_routes
from error_handlers import configure_error_handlers

app = FastAPI()

@app.get("/")
async def health():
    return {
        'status_code': 200
    }

configure_error_handlers(app)
configure_routes(app)
