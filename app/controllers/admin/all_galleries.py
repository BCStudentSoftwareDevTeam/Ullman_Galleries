from . import admin
from app.logic.validation import *
from flask import session
from flask import render_template
from app.models.Galleries import *
from app.models.Forms import *
from app.models.queries.GalleryQueries import *

@admin.route('/', methods=["GET","POST"])
def all_galleries():
    galleries = (Galleries
                    .select(Galleries, fn.Count(Forms.fid).alias('count'))
                    .join(Forms, JOIN.LEFT_OUTER)
                    .group_by(Galleries))

    status = dict()

    for gallery in galleries: 
        status[gallery.title] = get_status(gallery.gid)

    return render_template('views/admin/all_galleries.html',status=status, galleries=galleries)


