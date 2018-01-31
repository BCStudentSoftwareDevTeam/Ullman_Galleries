from app.models.util import *
from app.models.Files import *

class Galleries (baseModel):
  gid           = IntegerField(primary_key=True)
  title         = TextField()
  open_date     = DateTimeField()
  close_date    = DateTimeField()
  description   = TextField()
  banner        = ForeignKeyField(Files)

  def __str__(self):
    return self.gid
