from dataclasses import field
from enum import unique
import imp
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Optional, Iterable
from tortoise.backends.base.client import BaseDBAsyncClient
from utils.hash import get_hashed_password

class User(Model):
    id= fields.BigIntField(pk=True)
    username= fields.CharField(50)
    email = fields.CharField(80, null=True)
    password = fields.CharField(256)
    is_active= fields.BooleanField(default=True)
    created = fields.DatetimeField(auto_now=True)
    updated = fields.DatetimeField(auto_now_add=True)

    async def save(self, using_db: Optional[BaseDBAsyncClient] = None, update_fields: Optional[Iterable[str]] = None, force_create: bool = False, force_update: bool = False) -> None:
        self.password=get_hashed_password(self.password)
        return await super().save(using_db, update_fields, force_create, force_update)


userIn_pydantic = pydantic_model_creator(User, name='userIn', exclude=['id', 'is_active', 'created','updated'])
userOut_pydantic=pydantic_model_creator(User, name='userOut', exclude=['password'])