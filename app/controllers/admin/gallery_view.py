from . import admin
from app.logic.validation import *
from flask import session
from flask import abort
from flask import send_file
from flask import current_app
from flask import render_template
from flask import flash 
from flask_security import login_required
import shutil
import bleach


@admin.route('/gallery/description', methods=["POST"])
@login_required
def change_description():
    description = request.form['description']
    gid = 1
    gallery = GalleryQueries.get(gid)
    gallery.description = description
    gallery.save()
    flash("Description Updated", "success")
    return bleach.clean(description)

@admin.route('/view/', methods=["GET"])
@login_required
def gallery_view():
    gid = 1
    gallery = GalleryQueries.get(gid)
    forms = FormQueries.get_all_from_gallery(gallery.gid) 
    description = gallery.description
    if description is not None:
        description = description.strip()
    is_admin = doesUserHaveRole('admin')
    return render_template('views/admin/gallery_view.html', description= description, forms = forms, gallery = gallery, is_admin=is_admin)

@admin.route('/view/<int:form_id>', methods=["GET","POST"])
@login_required
def view_form(form_id):
    session['form_id'] = form_id
    return redirect('review')

@admin.route('/view/next', methods=["GET"])
@login_required
def next_form():
    session['form_id'] = session['form_id'] + 1
    return redirect('review')

@admin.route('/view/previous', methods=["GET"])
@login_required
def previous_form():
    session['form_id'] = session['form_id'] - 1
    return redirect('review')

@admin.route('/view/download/<int:form_id>', methods=["GET"])
@login_required
def download_user_form(form_id):
    session['form_id'] = form_id
    return redirect('download/user')

@admin.route('/delete/all')
@login_required
def delete_all():
    gid = 1
    zipfile = get_zip_of_files()
    if zipfile is not None:
        forms = FormQueries.get_all_from_gallery(gid, True)
        for form in forms:
            filepath = current_app.root_path + form.folder_path
            if os.path.exists(filepath):
                shutil.rmtree(filepath)
            form.status = "Deleted"
            form.save()
        flash("Files Deleted","success")
        return send_file(zipfile, as_attachment=True)

@admin.route('/download/all')
@login_required
def download_all():
    zipfile = get_zip_of_files()
    if zipfile is not None:
        return send_file(zipfile, as_attachment=True)
    abort(404)

def get_zip_of_files():
        form = FormQueries.get(1)
        filepath = current_app.root_path + "/static/data/" + form.gallery.folder_name + "/"
        if os.path.exists(filepath):
            zip_archive = filepath + "/../archive/%s-full-backup"  % (form.gallery.title)
            zipfile = shutil.make_archive(zip_archive, "zip", filepath)
            return zipfile
        return None
