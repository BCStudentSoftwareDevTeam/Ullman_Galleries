from . import admin
from app.logic.validation import *
from flask import session
from flask import abort
from flask import send_file
from flask import current_app
from flask import render_template
from flask import flash 
from app.models.queries import UserQueries
from flask_security import login_required
from flask import current_app
from flask_security.utils import hash_password,verify_password
import shutil
import bleach

@admin.route('/users/add', methods=["POST"])
@login_required
def add_user():
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']

    if password == confirm:
        datastore = current_app.extensions['security'].datastore
        datastore.create_user(email=email, password=hash_password(password), role="admin")
        flash("User Created", "success")
    else:
        flash("Passwords must match", "fail")
    return redirect("/view")

@admin.route('/users/remove', methods=["POST"])
@login_required
def remove_user():
    datastore = current_app.extensions['security'].datastore
    email = request.form['email']
    user = datastore.get_user(email)
    datastore.delete_user(user)
    flash("User Removed", "success")
    return redirect("/view")

@admin.route('/users/change_password', methods=["POST"])
@login_required
def change_password():
    password = request.form['password']
    confirm = request.form['confirm']
    current = request.form['current']

    if password == confirm :
        user_id = session["user_id"]
        datastore = current_app.extensions['security'].datastore
        user = datastore.get_user(user_id)
        verify = verify_password(current,user.password)
        if verify:
            user.password = hash_password(password)
            user.save()
            flash("Your password has been updated", "success")
        else:
            flash("The password supplied was incorrect","danger")
        return redirect("/view/")
    else:
        flash("Passwords must match","danger")
        return redirect("/view/")



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
    users = UserQueries.select_all()
    return render_template('views/admin/gallery_view.html', users=users, description= description, forms = forms, gallery = gallery, is_admin=is_admin)

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
