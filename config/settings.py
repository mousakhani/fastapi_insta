from jose.constants import ALGORITHMS


class Settings:
    DATABASE_HOST='localhost'
    DATABASE_NAME='insta'
    DATABASE_USER='morteza'
    DATABASE_PASS='admin'
    SECRET_KEY='e4@s8JbUpnpX2Xs9ep2sr08955t43Dq^h^lLPG@VpdEXdctjaU'
    TOKEN_EXPIRE_TIME_SECONDS= 7*24*60 # 7 days
    JWT_ALGORITHM= ALGORITHMS.HS512


settings= Settings()

DATABASE_URL=f'postgres://{settings.DATABASE_USER}:{settings.DATABASE_PASS}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}'


DATABASE_MODELS=[
    'aerich.models',
    'models.user',
    'models.post',
    'models.comment',
    ]


TORTOISE_ORM = {
    "connections": {
         "default": DATABASE_URL
    },
    "apps": {
        "contact": {
            "models":DATABASE_MODELS,
            "default_connection": "default",
        },
    },
}