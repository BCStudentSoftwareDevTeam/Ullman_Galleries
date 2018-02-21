from . import public 
from app.logic.validation import *
from flask import render_template
from flask import session
from app.models.Forms import Forms
from app.models.queries.FilesQueries import*
from app.models.queries.FormQueries import *
from flask import send_file
from flask import current_app
from flask import send_from_directory 

@public.route('/application/review/', methods=["GET", "POST"])
def review():
    fid = session['form_id']
    form = FormQueries.get(fid)
    return render_template('views/public/application_review.html', form = form)


@public.route('/download/cv/', methods=["GET","POST"])
def download():
    fid = session['form_id']
    cv = FormQueries.get_cv(fid)
    filepath = current_app.root_path + cv.filepath
    filename = "%s.%s" % (cv.filename, cv.filepath)
    return send_file(filepath, as_attachment = True, attachment_filename=filename)

@public.route('/download/statement/', methods=["GET","POST"])
def download_statement():
    fid = session['form_id']
    statement = FormQueries.get_statement(fid)
    filepath = current_app.root_path + statement.filepath
    filename = "%s.%s" % (statement.filename, statement.filetype)
    return send_file(filepath, as_attachment = True, attachment_filename=filename)

