import logging
from fastapi.responses import StreamingResponse, Response
from fastapi import APIRouter, Request, Header, Form, HTTPException, UploadFile, File, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasicCredentials
from fastapi.params import  Query
from fastapi.responses import HTMLResponse
from app.services import Chat
from app.services.chat_service import authenticate_user
from fastapi.templating import Jinja2Templates
from app.services.session_manage import session_manager

log = logging.getLogger("chat")
chatRouter = APIRouter(prefix="/chat", tags=["admin"])

templates = Jinja2Templates(directory="templates")
admin_instance = Chat()


@chatRouter.post("/login")
def login(response: Response, user: dict = Depends(authenticate_user)):
    session_id = session_manager.create_session(user)
    # Get existing sessions for the user
    existing_sessions = session_manager.get_user_sessions(user)
    
    return {"message": "Login successful", "session_id": session_id, "existing_sessions": existing_sessions}

@chatRouter.post("/logout")
def logout(session_id: str):
    session_manager.delete_session(session_id)
    return {"message": "Logout successful"}

@chatRouter.get("/")
async def get_chat(request: Request, user_input: str, session_id: str = ""):
    
    if not session_id:
        raise HTTPException(status_code=401, detail="Session ID not found")
    
    chat = await admin_instance.unhelpful_chatbot(user_input, session_id)
    return chat

@chatRouter.get("/history")
async def get_chat(request: Request, session_id: str = "", user: dict = Depends(authenticate_user)):
    
    if not session_id:
        raise HTTPException(status_code=401, detail="Session ID not found")
    
    # Verify if the session ID belongs to the authenticated user
    if session_manager.get_user(session_id) != user:
        raise HTTPException(status_code=403, detail="Unauthorized access")
    
    chat = await admin_instance.get_history(session_id)
    return chat

@chatRouter.get("/signin", response_class=HTMLResponse)
async def login(
    request: Request,
    ):
    return templates.TemplateResponse("index.html", {"request": request})

@chatRouter.get("/main", response_class=HTMLResponse)
async def login(
    request: Request,
    ):
    return templates.TemplateResponse("chat.html", {"request": request})