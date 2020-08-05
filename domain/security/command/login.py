from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class ActionTokenModel(BaseModel):
    token: str

class AdminActions(BaseModel):
    createTopic: ActionTokenModel
    renameTopic: ActionTokenModel
    deleteTopic: ActionTokenModel

class AdminLoggedIn(BaseModel):
    actions: AdminActions
    
class StudentLoggedIn(BaseModel):
    token: str

class Empty(BaseModel):
    pass

class LoginResponse(BaseModel):
    result_type: str
    STUDENT_LOGGED_IN: Optional[StudentLoggedIn] = Field(
        None,
        description="Fields for when a student logs in"
    )
    ADMIN_LOGGED_IN: Optional[AdminLoggedIn] = Field(
        None,
        description="Fields for when an administrator logs in"
    )

@router.post(
    "/api/security/command/login",
    tags=["security"],
    response_model=LoginResponse)
async def login(body:LoginRequest):
    return {
        "result_type": "LOGIN_SUCCESSFULL",
        "LOGIN_SUCCESSFULL": {
            "token": "1234",
            "actions": [ ]
        }
    }