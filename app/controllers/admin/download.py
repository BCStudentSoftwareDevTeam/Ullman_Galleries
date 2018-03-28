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
from datetime import datetime
import shutil
import bleach
import csv
import io


@admin.route('/download/all/')
@login_required
def download_all():
    forms = FormQueries.get_all_from_gallery(1)
    filepath = generate_csv(forms)
    zipfile = get_zip_of_files()
    if zipfile is not None:
        return send_file(zipfile, as_attachment=True)
    return abort(404)


@admin.route('/download/contact-info/', methods=['GET'])
@login_required
def contact_info():
    gid = 1
    forms = FormQueries.get_all_from_gallery(gid)
    filepath = generate_csv(forms)
    if filepath is not None:
        return send_file(
            filepath,
            as_attachment=True,
            attachment_filename='contact-info.csv')
    return abort(404)


def generate_csv(forms):
    if len(forms) > 0:
        entries = [
            'first_name', 'last_name', 'street_address', 'second_address',
            'city', 'state', 'zip_code', 'email', 'phone_number', 'website',
            'submit_date', 'status'
        ]
        header = ",".join(entries)
        filepath = get_static_absolute_path(forms[0].gallery.folder_name,
                                            'contact-info.csv')
        with open(filepath, 'w') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=entries, extrasaction="ignore")
            writer.writeheader()
            for entry in forms:
                writer.writerow(entry.__data__)
        return filepath
    return None

def get_zip_of_files():
    form = FormQueries.get_all_from_gallery(1,True)[0]
    if form is not None:
        filepath = get_static_absolute_path(form.gallery.folder_name)
        if os.path.exists(filepath):
            date = str(datetime.today().__format__("%m-%d-%y"))
            zip_archive = filepath + \
                "/../archive/%s-%s-full-backup" % (date,form.gallery.title)
            zipfile = shutil.make_archive(zip_archive, "zip", filepath)
            return zipfile
    return None
