from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session
from datetime import datetime

@app.route('/gallery/edit/<int:gid>', methods=["GET","POST"])
#@require_role('admin')
def gallery_edit(gid):
    if request.method == "GET":
        gallery = GalleryQueries.get(gid)
        if gallery is not None:
            return render_template('views/gallery_edit.html', gallery=gallery)
        else:
            abort(404)
    if request.method == "POST":
        galleryData = request.form
        #TODO: need to sanitize description
        #TODO: need to validate form date format
        updatedGid = GalleryQueries.update(gid,\
                                    galleryData['title'],\
                                    datetime.strptime(galleryData['open_date'],'%m/%d/%Y'),\
                                    datetime.strptime(galleryData['close_date'],'%m/%d/%Y'),\
                                    galleryData['description'],\
                                    galleryData['banner'])
        if updatedGid is not None:
            print("update success") #TODO: replace with some flash
            return redirect(url_for('gallery_edit', gid=updatedGid))
        else:
            print("update failed") #TODO: replace with some flash
            return redirect(url_for('gallery_edit', gid=gid))
            