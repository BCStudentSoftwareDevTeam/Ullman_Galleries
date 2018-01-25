from app.models.util import *

class Users (baseModel):
  uid               = PrimaryKeyField()
  username          = TextField()

