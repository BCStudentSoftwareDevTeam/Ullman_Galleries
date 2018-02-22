from . import admin
from app.logic.validation import *
from flask import session
from flask import render_template

@admin.route('/view/', methods=["GET"])
def gallery_view():
    gid = 1
    gallery = GalleryQueries.get(gid)
    forms = FormQueries.get_all_from_gallery(gallery.gid) 
    is_admin = False
    if(doesUserHaveRole('admin')):
        is_admin = True
    return render_template('views/admin/gallery_view.html', forms = forms, gallery = gallery, is_admin=is_admin)

@admin.route('/view/<int:form_id>', methods=["GET","POST"])
def view_form(form_id):
    session['form_id'] = form_id
    return redirect('review')

@admin.route('/view/next', methods=["GET"])
def next_form():
    session['form_id'] = session['form_id'] + 1
    return redirect('review')

@admin.route('/view/previous', methods=["GET"])
def previous_form():
    session['form_id'] = session['form_id'] - 1
    return redirect('review')

@admin.route('/view/download/<int:form_id>', methods=["GET"])
def download_user_form(form_id):
    session['form_id'] = form_id
    return redirect('download/user')
    

