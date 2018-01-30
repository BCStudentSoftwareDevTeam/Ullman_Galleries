from app.allImports import * 
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/gallery/submission/<int:gid>', methods=["GET","POST"])
def gallery_submission(gid):
    gallery = GalleryQueries.get(gid)
    #TODO sanatize html data
    is_admin = False
    if(doesUserHaveRole('admin')):
        is_admin = True
    return render_template('views/gallery_submission.html', gallery=gallery, is_admin=is_admin)




