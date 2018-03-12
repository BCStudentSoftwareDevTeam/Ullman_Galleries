from app.models.util import *
from flask_security import UserMixin 


class Users (baseModel, UserMixin):
  # uid               = PrimaryKeyField()
  email             = TextField()
  password          = TextField()
  active            = BooleanField(default=True)
  confirmed_at      = DateTimeField(null=True)

