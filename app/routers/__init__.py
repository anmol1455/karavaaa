from fastapi import APIRouter

from .chat import chatRouter

router = APIRouter()

router.include_router(chatRouter)