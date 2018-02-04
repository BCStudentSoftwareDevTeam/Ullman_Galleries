from . import admin
from app.logic.validation import *
from app.logic.upload import gallery_banner_upload
from flask import render_template
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
        fid = gallery_banner_upload(request, galleryData['title'], gallery.banner.fid)

        #TODO: need to sanitize de@scription
        #TODO: need to validate form date format
        updatedGid = GalleryQueries.update(gid,\
                                    galleryData['title'],\
                                    datetime.strptime(galleryData['open_date'],'%m/%d/%Y'),\
                                    datetime.strptime(galleryData['close_date'],'%m/%d/%Y'),\
                                    galleryData['description'],\
                                    fid)
        if updatedGid is not None:
            print("update success") #TODO: replace with some flash
            return redirect(url_for('administrator.gallery_edit', gid=updatedGid))
        else:
            print("update failed") #TODO: replace with some flash
            return redirect(url_for('administrator.gallery_edit', gid=gid))
            
