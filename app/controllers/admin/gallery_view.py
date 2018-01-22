from . import admin
from app.logic.validation import *
from flask import render_template

@admin.route('/gallery/view', methods=["GET","POST"])
def gallery_view():
    return render_template('views/gallery_view.html')
