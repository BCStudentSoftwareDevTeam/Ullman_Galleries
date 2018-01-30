from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/gallery/view', methods=["GET","POST"])
def gallery_view():
    gid = 1
    gallery = GalleryQueries.get(gid)
    is_admin = False
    if(doesUserHaveRole('admin')):
        is_admin = True
    return render_template('views/gallery_view.html', gallery = gallery, is_admin=is_admin)

