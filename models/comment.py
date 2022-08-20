from tortoise.models import Model
from tortoise import fields

class Comment(Model):
    id = fields.IntField(pk=True)
    title=fields.CharField(40,)
    created = fields.DatetimeField(auto_now=True)
    updated= fields.DatetimeField(auto_now_add=True)