from app.models.util import *
from app.models.Files import *
from datetime import datetime

class Galleries (baseModel):
  gid           = IntegerField(primary_key=True)
  title         = TextField()
  open_date     = DateTimeField()
  close_date    = DateTimeField()
  description   = TextField()
  banner        = ForeignKeyField(Files)

  def __str__(self):
    return self.title
    
    
  def GalleryStatus(self):
    '''Determines the status for each gallery instance'''
    status ={}
    galleries=Galleries.select()
    today = datetime.now()
    for gallery in galleries:
      openDate = gallery.open_date
      closeDate = gallery.close_date
      if today >= openDate and today >= closeDate: #if gallery closed,status = closed
        status[str(gallery)]="Closed" + " " + str(closeDate)
      if today <= openDate and today <= closeDate: #if gallery not open but coming soon, status = coming soon
        status[str(gallery)] = "Coming Soon " +" " + str(openDate)
      if today >= openDate and today <= closeDate: #if gallery open, status = active
        status[str(gallery)]= "Active " + " " + str(openDate) + " " + "to" + " " + str(closeDate)
          
    return status


    

