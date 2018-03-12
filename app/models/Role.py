from app.models.util import *
from flask_security import RoleMixin

class Role (baseModel, RoleMixin):
  # rid               = PrimaryKeyField()
  name              = CharField(unique=True)
  description       = TextField(null=True)
