from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/gallery/submission', methods=["GET","POST"])
def gallery_submission():
    return render_template('views/gallery_submission.html')




