import asyncio
from typing import List
from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from core.exceptions import CustomException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router
from fastapi.staticfiles import StaticFiles


def init_routers(karvaaa: FastAPI):
    karvaaa.include_router(router)


def init_cors(karvaaa: FastAPI):
    karvaaa.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_headers=["*"],
        allow_methods=["*"],
        allow_credentials=True
    )


def init_middleware(karvaaa: FastAPI):
    pass

def init_listeners(karvaaa: FastAPI):
    @karvaaa.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message}
        )


def create_app() -> FastAPI:
    karvaaa = FastAPI(
        title="karvaaa test api",
        description="karvaaa test",
        version="0.1",
        docs_url="/active-docs",
    )
    # init_middleware(pineapple_app)
    init_routers(karvaaa)
    init_listeners(karvaaa)
    init_cors(karvaaa)
    return karvaaa


karvaaa = create_app()
karvaaa.mount("/static", StaticFiles(directory="static"), name="static")


@karvaaa.on_event("startup")
async def bootstrapping():
    print("we can schedule a connection listener here")

