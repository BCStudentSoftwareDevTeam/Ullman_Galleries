from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/application/create', methods=["GET","POST"])
def create():
    return render_template('views/application_create.html')



@app.route('/application/submit', methods=["POST"])
def application_submit():
    data        = request.form
    submit_date = time.strftime("%m%d%y")
    try:
        #Insert data into database
        submission = 
    except Exception as e:
        print e
        flash ("An error occured during submission.")
        return redirect(url_for("/"))
        

