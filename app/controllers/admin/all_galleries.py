from . import admin
from app.logic.validation import *
from app.models.Forms import *

from flask import render_template
@admin.route('/', methods=["GET","POST"])
def all_galleries():
    user = Forms.get(fid=1)
    name = user.first_name
    print(name)
    print(doesUserHaveRole("admin"))
    return render_template('views/all_galleries.html')


