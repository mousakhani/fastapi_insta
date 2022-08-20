from tkinter.messagebox import NO
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User
from utils.hash import verify_password
from auth.oauth2 import create_token

route = APIRouter(
    prefix='/token',
    tags=['Authentication']
)


@route.post('/')
async def get_token(user_in: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(username=user_in.username)
    user_error = HTTPException(status_code=400, detail='username or password is incorrect')
    if user is None:
        raise user_error
    if verify_password(user_in.password, user.password):
        token= create_token({'id':user.id})
        return {
            'access_token':token,
            'token_type':'Bearer'
        }
    raise user_error
