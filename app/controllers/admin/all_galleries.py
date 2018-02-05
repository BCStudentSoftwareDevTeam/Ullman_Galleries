from . import admin
from app.logic.validation import *
from werkzeug.security import check_password_hash
from app.models.Forms import *
from flask import session
from app.models.Galleries import *
from flask import render_template
from app.models.queries.GalleryQueries import *

@admin.route('/', methods=["GET","POST"])
def all_galleries():
    
    gallery_submission_querry = (Galleries
                                .select(Galleries, fn.Count(Forms.fid).alias('count'))
                                .join(Forms, JOIN.LEFT_OUTER)
                                .group_by(Galleries))
         
    gallery_submissions_count ={}  
    status= {}
    
    for gallery in gallery_submission_querry:
        status[str(gallery)]= getstatus(gallery.gid)
        gallery_submissions_count[str(gallery)]=gallery.count 
        
    return render_template('views/admin/all_galleries.html',
                                                gallery_submissions_count=gallery_submissions_count,
                                                status=status,
                                                )


