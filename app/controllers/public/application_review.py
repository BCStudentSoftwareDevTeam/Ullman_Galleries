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


@public.route("/contributors/")
def contributors():
    return render_template("snips/contributors.html",
                        cfg = get_cfg()
                        )

@public.route('/withdraw', methods=["GET"])
def withdraw():
    fid = session['form_id']
    if fid is None:
        abort(404)
    form = FormQueries.get(fid)
    form.status = "Withdrew"
    form.save()
    flash("Your Application has been withdrawn", 'danger')
    return redirect('/')


@public.route('/success/', methods=["GET", "POST"])
def success():
    fid = session['form_id']
    if fid is None:
        abort(404)
    form = FormQueries.get(fid)
    form.status = "Completed"
    form.save()
    flash("Your Application has been submitted", "success")
    return redirect('/review')

@public.route('/review/', methods=["GET", "POST"])
def review():
    gid = 1
    fid = session['form_id']
    if fid is None:
        abort(404)
    form = FormQueries.get(fid)
 
    files = FormToFileQueries.get_form_files(fid)

    show_next = False
    show_previous = False
    is_admin = doesUserHaveRole('admin')
    if len(FormQueries.get_all_from_gallery(gid)) > (fid):
        show_next = True
    if fid != 1:
        show_previous = True
    cfg = get_cfg()

    return render_template('views/public/application_review.html', form = form, files = files, allowed_extensions = cfg['allowed_extensions'], document_extensions = cfg['document_extensions'], is_admin=is_admin, show_next= show_next, show_previous=show_previous)


@public.route('/download/cv/', methods=["GET","POST"])
def download():
    fid = session['form_id']
    if fid is None:
        abort(404)
    cv = FormQueries.get_cv(fid)
    filepath = current_app.root_path + cv.filepath
    return send_file(filepath, as_attachment = True, attachment_filename=cv.filename)

@public.route('/download/user')
def download_user():
    fid = session['form_id']
    if fid is None:
        abort(404)
    form = FormQueries.get(fid)
    filepath = current_app.root_path + form.folder_path
    zip_archive = current_app.root_path + form.folder_path + "/../../archive/%s-%s" % (form.first_name, form.last_name)
    zipfile = shutil.make_archive(zip_archive, "zip", filepath)
    return send_file(zipfile, as_attachment=True)



@public.route('/download/statement/', methods=["GET","POST"])
def download_statement():
    fid = session['form_id']
    if fid is None:
        abort(404)
    statement = FormQueries.get_statement(fid)
    filepath = current_app.root_path + statement.filepath
    filename = "%s.%s" % (statement.filename, statement.filetype)
    return send_file(filepath, as_attachment = True, attachment_filename=statement.filename)
