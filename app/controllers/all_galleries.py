from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session
from app.models.Forms import *
from app.models.Galleries import *
from datetime import datetime



@app.route('/', methods=["GET","POST"])
def all_galleries():
    gallerySubmissionQuerry = Galleries().select().join(Forms, JOIN_LEFT_OUTER).annotate(Forms) #gets all gallery submissions
    galleryTosubmissions ={}  #maps each gallery to the number of submissions it has e.g { Gallery-1 : 10-submissions }
    
  
    
    for gallery in gallerySubmissionQuerry:
        galleryStatus = gallery.GalleryStatus()  #gets gallery statuses 
        galleryTosubmissions[str(gallery)]=gallery.count 

    return render_template('views/all_galleries.html',
                                                galleryTosubmissions=galleryTosubmissions,
                                                galleryStatus=galleryStatus,
                                                )


