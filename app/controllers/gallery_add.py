from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session
from datetime import datetime

@app.route('/gallery/add', methods=["GET","POST"])
#@require_role('admin')
def gallery_add():
    if request.method == "GET":
        return render_template('views/gallery_edit.html')
    if request.method == "POST":
        galleryData = request.form
        #TODO: need to sanitize description
        #TODO: need to validate form date format
        gid = GalleryQueries.insert(galleryData['title'],\
                                    datetime.strptime(galleryData['open_date'],'%m/%d/%Y'),\
                                    datetime.strptime(galleryData['close_date'],'%m/%d/%Y'),\
                                    galleryData['description'],\
                                    galleryData['banner'])
        if gid is not None:
            print("create success") #TODO: replace with some flash
            return redirect(url_for('gallery_edit', gid=gid))
        else:
            print("create failed") #TODO: replace with some flash
            return redirect(url_for('gallery_add'))