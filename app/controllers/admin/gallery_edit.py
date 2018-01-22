from . import admin
from app.logic.validation import *
from flask import render_template


@admin.route('/gallery/edit', methods=["GET","POST"])
def gallery_edit():
    return render_template('views/gallery_edit.html')




