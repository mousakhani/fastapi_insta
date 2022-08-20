from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from datetime import  datetime, timedelta
from config.settings import settings
from models.user import User, userOut_pydantic
from jose import JWTError, jwt
from jose.constants import ALGORITHMS



oauth2_scheme= OAuth2PasswordBearer(tokenUrl='token')


def create_token(data: dict, token_expire_time_seconds: int=None):
    if token_expire_time_seconds:
        expire = token_expire_time_seconds
    else:
        expire = settings.TOKEN_EXPIRE_TIME_SECONDS
    to_encode= data.copy()
    to_encode.update({'exp':datetime.utcnow()+ timedelta(seconds=expire)})
    token = jwt.encode(to_encode, key=settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

async def get_current_user(token:str = Depends(oauth2_scheme)):
    token_error=HTTPException(status_code=401, detail='UnAuthorized')
    try:
        data= jwt.decode(token, key=settings.SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
        user_id= data.get('id')
    except:
        raise token_error
    return await userOut_pydantic.from_queryset_single(User.get(id=user_id))

def current_active_user(user_in: userOut_pydantic=Depends(get_current_user)):
    if user_in.is_active:
        return user_in
    raise HTTPException(status_code=403, detail='This user blocked')