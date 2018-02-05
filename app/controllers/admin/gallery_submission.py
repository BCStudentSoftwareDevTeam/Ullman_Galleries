from . import admin
from app.logic.validation import *
from flask import session
from flask import render_template

@admin.route('/gallery/submission/<int:gid>', methods=["GET","POST"])
def gallery_submission(gid):
    gallery = GalleryQueries.get(gid)
    #TODO sanatize html data
    is_admin = False
    if(doesUserHaveRole('admin')):
        is_admin = True
    return render_template('views/admin/gallery_submission.html', gallery=gallery, is_admin=is_admin)





