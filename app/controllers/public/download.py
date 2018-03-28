from . import public
from app.logic.validation import *
from flask import render_template
from flask import session
from app.models.Forms import Forms
from app.models.queries.FilesQueries import *
from app.models.queries.FormQueries import *
from app.models.queries.FormToFileQueries import *
from flask import send_file
from flask import abort
from flask import current_app
from flask import redirect
from flask import send_from_directory
from flask import flash
from app.config.loadConfig import get_cfg
import shutil


@public.route('/download/cv/', methods=["GET", "POST"])
def download_cv():
    fid = session['form_id']
    if fid is None:
        return abort(404)
    cv = FormQueries.get_cv(fid)
    filepath = get_static_absolute_path(cv.filepath)
    return send_file(
        filepath, as_attachment=True, attachment_filename=cv.filename)


@public.route('/download/user/')
def download_user():
    fid = session['form_id']
    print(fid)
    if fid is None:
        return abort(404)
    form = FormQueries.get(fid)
    filepath = get_static_absolute_path(form.folder_path)
    zip_archive = filepath + \
        "/../../archive/%s-%s-%s" % (form.first_name, form.last_name, form.fid)
    print(zip_archive)
    zipfile = shutil.make_archive(zip_archive, "zip", filepath)
    return send_file(zipfile, as_attachment=True)


@public.route('/download/statement/', methods=["GET", "POST"])
def download_statement():
    fid = session['form_id']
    if fid is None:
        return abort(404)
    statement = FormQueries.get_statement(fid)
    filepath = get_static_absolute_path(statement.filepath)
    filename = "%s.%s" % (statement.filename, statement.filetype)
    return send_file(
        filepath, as_attachment=True, attachment_filename=statement.filename)
