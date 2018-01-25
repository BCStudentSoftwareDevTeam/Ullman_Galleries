from app.allImports import * 
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session
from app.models.Forms import *

@app.route('/', methods=["GET","POST"])
def all_galleries():
    user = Forms.get(fid=1)
    name = user.first_name
    print(name)
    print(doesUserHaveRole("admin"))
    return render_template('views/all_galleries.html')


