from . import admin
from app.logic.validation import *
from flask import session
from flask import abort
from flask import send_file
from flask import current_app
from flask import render_template
from flask import flash
from app.models.queries import UserQueries
from flask_security import login_required, roles_required
from flask import current_app
from flask_security.utils import hash_password, verify_password
from app.controllers.public.status import change_status
from flask_security.core import current_user
import shutil
import bleach
import csv
import io



@admin.route('/view/', methods=["GET"])
@login_required
def gallery_view():
    gid = 1
    gallery = GalleryQueries.get(gid)
    forms = FormQueries.get_all_from_gallery(gallery.gid)
    description = gallery.description
    if description is not None:
        description = description.strip()
    users = UserQueries.select_all()
    return render_template(
        'views/admin/view.html',
        users=users,
        description=description,
        forms=forms,
        gallery=gallery)


@admin.route('/view/<int:form_id>', methods=["GET"])
@login_required
def view_form(form_id):
    session['form_id'] = form_id
    return redirect('application/review')

@admin.route('/view/status/change/<status>/<int:form_id>/', methods=["POST"])
@login_required
def view_status_change(status,form_id):
    session['form_id'] = form_id
    print("JS")
    return change_status(status)
    return redirect('/status/change/%s/'%(status))




@admin.route('/view/next', methods=["GET"])
@login_required
def next_form():
    session['form_id'] = session['form_id'] + 1
    return redirect('application/review')


@admin.route('/view/previous', methods=["GET"])
@login_required
def previous_form():
    session['form_id'] = session['form_id'] - 1
    return redirect('application/review')


@admin.route('/view/download/<int:form_id>', methods=["GET"])
@login_required
def download_user_form(form_id):
    session['form_id'] = form_id
    return redirect('download/user')


@admin.route('/view/description', methods=["POST"])
@login_required
def change_description():
    description = request.form['description']
    gid = 1
    gallery = GalleryQueries.get(gid)
    gallery.description = description
    gallery.save()
    flash("Description Updated", "success")
    return bleach.clean(description)
