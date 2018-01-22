from . import public
from app.logic.validation import *
from flask import render_template

@public.route('/application/review', methods=["GET","POST"])
def review():
    return render_template('views/application_review.html')




