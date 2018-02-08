from app.models.util import *
from app.models.Forms import *
from app.models.Files import Files

class Images (baseModel):
  iid               = PrimaryKeyField()
  form              = ForeignKeyField(Forms)
  fullsize          = ForeignKeyField(Files, related_name="fullsize")
  thumbnail        = ForeignKeyField(Files, related_name="thumbnail", null = True) # can be null just for now


