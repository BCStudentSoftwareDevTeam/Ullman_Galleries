from app.models.util import *
from app.models.Forms import *
from app.models.Files import Files

class Images (baseModel):
  iid               = IntegerField(primary_key=True)
  form              = ForeignKeyField(Forms)
  fullsize          = ForeignKeyField(Files, related_name="fullsize")
  thumbnail        = ForeignKeyField(Files, related_name="thumbnail")


