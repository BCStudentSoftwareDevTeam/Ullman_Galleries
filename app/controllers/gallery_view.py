from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session
from app.models.Forms import*
from app import render_template 


@app.route('/', methods=["GET","POST"])
def gallery_view():
    gallery= Forms.get(gid)
    is_admin = False
    if(doesUserHaveRole('admin')):
        is_admin = True
    return render_template('views/admin/gallery_submission.html', gallery=gallery, is_admin=is_admin)

    



