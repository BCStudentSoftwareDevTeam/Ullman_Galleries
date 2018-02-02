from . import admin
from app.logic.validation import *
from flask import session

@admin.route('/gallery/view/<int:gid>', methods=["GET","POST"])
def gallery_view(gid):
    gallery = GalleryQueries.get(gid)
    forms = FormQueries.get_all_from_gallery(gallery.gid)
    is_admin = False
    if(doesUserHaveRole('admin')):
        is_admin = True
    return render_template('views/admin/gallery_view.html', forms = forms, gallery = gallery, is_admin=is_admin)

