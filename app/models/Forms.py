from app.models.util import *
from app.models.Galleries import *
from app.models.Files import *
from peewee import *

class Forms (baseModel):
  fid               = PrimaryKeyField()
  first_name        = TextField()
  last_name         = TextField()
  street_address    = TextField()
  second_address    = TextField()
  city              = TextField()
  state             = TextField()
  zipCode           = TextField()
  email             = TextField()
  phone_number      = TextField()
  website           = TextField()
  gallery           = ForeignKeyField(Galleries)
  cv                = ForeignKeyField(Files, related_name="cv_file", null = True)
  personal_statement = ForeignKeyField(Files, related_name="personal_statment", null = True)
  submit_date       = CharField()

