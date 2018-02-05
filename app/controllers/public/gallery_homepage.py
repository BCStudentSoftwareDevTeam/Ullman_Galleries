from . import public
from app.logic.validation import *
from flask import render_template

@public.route('/homepage', methods=["GET","POST"])
def homepage():
    return render_template('views/public/gallery_homepage.html')




