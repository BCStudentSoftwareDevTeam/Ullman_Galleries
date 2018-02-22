from . import public 
from app.logic.validation import *
from flask import render_template 
from flask import session
from app.models.Forms import Forms
from app.models.queries.FilesQueries import * 
from app.models.queries.FormQueries import *
from app.models.queries.ImageQueries import *
from flask import send_file
from flask import current_app
from flask import send_from_directory 
import shutil


@public.route('/review/', methods=["GET", "POST"])
def review():
    gid = 1
    fid = session['form_id']
    form = FormQueries.get(fid)
    images = ImageQueries.get_form_images(fid)

    show_next = False
    show_previous = False
    is_admin = False

    if(doesUserHaveRole('admin')):
        is_admin = True
    if len(FormQueries.get_all_from_gallery(gid)) > (fid + 1):
        show_next = True
    if fid != 1:
        show_previous = True
    return render_template('views/public/application_review.html', form = form, images = images, is_admin=is_admin, show_next= show_next, show_previous=show_previous)


@public.route('/download/cv/', methods=["GET","POST"])
def download():
    fid = session['form_id']
    cv = FormQueries.get_cv(fid)
    filepath = current_app.root_path + cv.filepath
    return send_file(filepath, as_attachment = True, attachment_filename=cv.filename)

@public.route('/download/user')
def download_user():
    fid = session['form_id']
    form = FormQueries.get(fid)
    filepath = current_app.root_path + form.folder_path
    zip_archive = current_app.root_path + form.folder_path + "/../archive/%s-%s" % (form.first_name, form.last_name)
    zipfile = shutil.make_archive(zip_archive, "zip", filepath)
    return send_file(zipfile, as_attachment=True)

@public.route('/download/statement/', methods=["GET","POST"])
def download_statement():
    fid = session['form_id']
    statement = FormQueries.get_statement(fid)
    filepath = current_app.root_path + statement.filepath
    filename = "%s.%s" % (statement.filename, statement.filetype)
    return send_file(filepath, as_attachment = True, attachment_filename=statement.filename)
