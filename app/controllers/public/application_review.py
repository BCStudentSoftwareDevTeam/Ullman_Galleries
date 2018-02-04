from . import public
from app.logic.validation import *
from flask import render_template

from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from app.models.Forms import Forms
from flask import session
from flask import \
    render_template, \
    request, \
    url_for, \
    Markup, \
    redirect

@public.route('/application/review/<fid>', methods=["GET","POST"])
def review(fid):
    user = Forms.get(fid==fid)
    return render_template('views/public/application_review.html', fid=fid, user = user)




