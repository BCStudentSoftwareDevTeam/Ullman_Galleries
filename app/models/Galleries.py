from app.models.util import *
from app.models.Files import *

class Galleries (baseModel):
  gid             = PrimaryKeyField()
  title           = TextField()
  open_date       = DateTimeField(null=True)
  close_date      = DateTimeField(null=True)
  description     = TextField(null=True)
  banner          = ForeignKeyField(Files, null=True)
  folder_name     = TextField(null=True)

  def __str__(self):
    return self.title
