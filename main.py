from fastapi import FastAPI

from routes import configure_routes
app = FastAPI()

@app.get("/")
async def health():
    return {
        'status_code': 200
    }

configure_routes(app)
