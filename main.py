from fastapi import FastAPI

from routes import configure_routes
app = FastAPI()

configure_routes(app)
