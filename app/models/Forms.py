from app.models.util import *
from app.models.Galleries import *
from app.models.Files import *
from peewee import *

class Forms (baseModel):
  fid               = IntegerField(primary_key=True)
  first_name        = TextField()
  last_name         = TextField()
  street_address    = TextField()
  city              = TextField()
  state             = TextField()
  email             = TextField()
  phone_number      = TextField()
  website           = TextField()
  gallery           = ForeignKeyField(Galleries)
  cv                = ForeignKeyField(Files, related_name="cv_file")
  personal_statement = ForeignKeyField(Files, related_name="personal_statment")
  submit_date       = CharField()
  status            = CharField(max_length=100)

