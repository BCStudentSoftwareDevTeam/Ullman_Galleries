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
        return self.title

class galleriesQueries():
    def select_single(self, gid):
        try:
            form = Galleries.get(Galleries.gid == gid)
            return form
        except Exception as e:
            print (e)
            return False
    
    def insert(self, title, open_date, close_date, description, ):
        try:
            gallery = Galleries(title=title,open_date=open_date,close_date=close_date,description=description)
        except Exception as e:
            print (e)
            return False