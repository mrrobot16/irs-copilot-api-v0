from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from starlette.exceptions import HTTPException as StarletteHTTPException

from db.error_handling_model import UnicornException, HorseException

def configure_error_handlers(app: FastAPI):
    @app.exception_handler(UnicornException)
    async def unicorn_exception_handler(request: Request, exc: UnicornException):
        return JSONResponse(
            status_code=418,
            content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
        )
    
    @app.exception_handler(HorseException)
    async def unicorn_exception_handler(request: Request, exc: UnicornException):
        return JSONResponse(
            status_code=418,
            content={"message": f"Oops! {exc.name} did something. There goes a farm..."},
        )
   
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
        return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request, exc):
        print(f"OMG! An HTTP error!: {repr(exc)}")
        return await http_exception_handler(request, exc)
    
    # NOTE: This exception wont run because below is another one 
    # which will override this exception since they both have same names
    # and raise "RequestValidationError".
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        print(f"OMG! The client sent invalid data!: {exc}")
        return await request_validation_exception_handler(request, exc)