from app.models.util import *
from app.models.Forms import *
from app.models.Files import Files

class FormToFile (baseModel):
  ftf               = PrimaryKeyField()
  form              = ForeignKeyField(Forms)
  file          = ForeignKeyField(Files, related_name="file",on_delete="CASCADE")


