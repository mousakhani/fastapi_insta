from tortoise.models import Model
from tortoise import fields

class Post(Model):
    id = fields.UUIDField(pk=True)
    title=fields.CharField(40)
    created=fields.DatetimeField(auto_now=True)