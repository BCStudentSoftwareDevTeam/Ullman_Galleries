from app.models.util import *
from app.models.Role import Role
from app.models.Users import Users

class UserRoles (baseModel):
  # urid              = PrimaryKeyField()
  user              = ForeignKeyField(Users, related_name = 'roles')
  role              = ForeignKeyField(Role, related_name = 'Users')
  name              = property(lambda self: self.role.name)
  description       = property(lambda self: self.role.description)
