from . import admin
from app.logic.validation import *
<<<<<<< HEAD:app/controllers/gallery_edit.py
from app.logic.upload import *
from werkzeug.security import check_password_hash
=======
from flask import render_template
>>>>>>> origin/development:app/controllers/admin/gallery_edit.py
from flask import session
from datetime import datetime

@admin.route('/gallery/edit/<int:gid>', methods=["GET","POST"])
#@require_role('admin')
def gallery_edit(gid):
    if request.method == "GET":
        gallery = GalleryQueries.get(gid)
        if gallery is not None:
            return render_template('views/admin/gallery_edit.html', gallery=gallery)
        else:
            abort(404)
    if request.method == "POST":
        gallery = GalleryQueries.get(gid)
        galleryData = request.form
        uploaded_path = gallery_banner_upload(request, galleryData['title'])
        #uploaded_path = upload(request, 'app/static/data')
        # create a function that gets the file id


        #TODO: need to sanitize de@scription
        #TODO: need to validate form date format
        updatedGid = GalleryQueries.update(gid,\
                                    galleryData['title'],\
                                    datetime.strptime(galleryData['open_date'],'%m/%d/%Y'),\
                                    datetime.strptime(galleryData['close_date'],'%m/%d/%Y'),\
                                    galleryData['description'],\
                                    2)
        if updatedGid is not None:
            print("update success") #TODO: replace with some flash
            return redirect(url_for('administrator.gallery_edit', gid=updatedGid))
        else:
            print("update failed") #TODO: replace with some flash
            return redirect(url_for('administrator.gallery_edit', gid=gid))
            
