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
from flask_security.core import current_user
from app.controllers.admin.download import get_zip_of_files
import shutil
import bleach
import csv
import io


@admin.route('/delete/all/')
@login_required
@roles_required("admin")
def delete_all():
    gid = 1
    zipfile = get_zip_of_files()
    if zipfile is not None:
        forms = FormQueries.get_all_from_gallery(gid, True)
        for form in forms:
            filepath = get_static_absolute_path(form.gallery.folder_name)
            FormToFileQueries.delete_all_files(form)
            if os.path.exists(filepath):
                shutil.rmtree(filepath)
            form.status = "Deleted"
            form.save()
        flash("Files Deleted", "success")
        redirect("/view/")
        return send_file(zipfile, as_attachment=True)
