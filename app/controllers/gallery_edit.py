from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/gallery/edit', methods=["GET","POST"])
def gallery_edit():
    return render_template('views/gallery_edit.html')




