from app.models.util import *
from app.models.Galleries import *
from app.models.Files import *
from peewee import *


class Forms (baseModel):
    fid               = PrimaryKeyField()
    first_name        = TextField()
    last_name         = TextField()
    street_address    = TextField()
    second_address    = TextField(null=True)
    city              = TextField()
    state             = TextField()
    zip_code           = TextField()
    email             = TextField()
    phone_number      = TextField(null=True)
    website           = TextField(null=True)
    gallery           = ForeignKeyField(Galleries)
    cv                = ForeignKeyField(Files, related_name="cv_file", null = True)
    personal_statement = ForeignKeyField(Files, related_name="personal_statment", null = True)
    submit_date       = DateTimeField()
    status            = TextField(null=True)

