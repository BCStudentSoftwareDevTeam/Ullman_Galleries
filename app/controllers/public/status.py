from . import public
from app.logic.validation import *
from flask import render_template
from flask import session
from app.models.Forms import Forms
from app.models.queries.FilesQueries import *
from app.models.queries.FormQueries import *
from app.models.queries.FormToFileQueries import *
from flask import send_file
from flask import abort
from flask import current_app
from flask import redirect
from flask import send_from_directory
from flask import flash
from app.config.loadConfig import get_cfg
import shutil


@public.route('/status/change/<status>/', methods=["POST"])
def change_status(status):
    fid = session['form_id']
    if fid is None:
        flash("Unable to withdraw the application", 'danger')
    else:
        form = FormQueries.get(fid)
        if form is not None:
            username = form.first_name + " " + form.last_name
            if status == "withdraw":
                form.status = "withdraw"
                flash("%s's application has been withdrawn" % (username), 'danger')
            elif status == "complete":
                form.status = "complete"
                flash("%s's application has been completed" % (username),
                      'success')
            elif status == "reject":
                form.status = "reject"
                flash("%s's application has been rejected" % (username), 'danger')
            elif status == "pending":
                form.status = "pending"
                flash("%s's application is now pending" % (username), 'success')
            elif status == "approve":
                form.status = "approve"
                flash("%s's application has been approved" % (username), 'success')
            elif status == "other":
                form.status = "other"
                flash("%s's application has been marked as other" % (username),
                      'warning')
            form.save()
        else:
            flash("Unable to withdraw the application", 'danger')

    return "OK"
