from . import public
from app.logic.validation import *
from flask import render_template
from app.models.Forms import Forms
from app.models.queries.FilesQueries import*
from app.models.queries.FormQueries import *
from flask import send_file

@public.route('/application/review/<int:fid>', methods=["GET", "POST"])
def review(fid):
    form = FormQueries.get(fid)
    return render_template('views/public/application_review.html', form = form)


@public.route('/download/cv/<int:fid>', methods=["GET","POST"])
def download(fid):
    filepath = get_file_path(fid)
    return send_file(filepath,attachment_filename= 'cv.pdf')

    

    