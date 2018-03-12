
from app.models.util import *
class Files (baseModel):
  fid           = PrimaryKeyField()
  filepath      = TextField()
  filename      = TextField()
  filetype      = TextField()

  def __str__(self):
    return self.filepath

