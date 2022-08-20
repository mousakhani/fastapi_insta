from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config.settings import DATABASE_URL, DATABASE_MODELS
from routers.user import route as user_route
from routers.authentication import route as auth_route
import uvicorn


app = FastAPI()

register_tortoise(
    app, 
    db_url=DATABASE_URL,
    modules={
        'models':DATABASE_MODELS
    },
    generate_schemas=False,
    add_exception_handlers=True,
)


app.include_router(user_route)
app.include_router(auth_route)


if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8000)