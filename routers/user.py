from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from auth.oauth2 import current_active_user
from models.user import User, userIn_pydantic, userOut_pydantic


route= APIRouter(
    prefix='/users',
    tags=['Users']
)

@route.post('/')
async def create_user(userIn: userIn_pydantic):
    user = await User.create(**userIn.dict())
    return await userOut_pydantic.from_tortoise_orm(user)


@route.get('/')
async def get_all_users(current_user:userOut_pydantic=Depends(current_active_user)):
    return current_user

def common_parameters(id:int, q: str | None = None, limit: int=0):
    return {'q':q, 'limit':limit, 'ids':id}

def is_admin():
    raise HTTPException(status_code=400, detail='Test Depends')


@route.get('/{id}')
async def test_depends(commons = Depends(is_admin)):
    return commons