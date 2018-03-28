from . import admin
from app.logic.validation import *
from flask import session
from flask import abort
from flask import send_file
from flask import current_app
from flask import render_template
from flask import flash
from app.models.queries import UserQueries
from flask_security import login_required, roles_required
from flask import current_app
from flask_security.utils import hash_password, verify_password
from flask_security.core import current_user
import shutil
import bleach
import csv
import io


@admin.route('/bye', methods=["GET"])
@login_required
def bye():
    session["form_id"] = None
    return redirect("/logout")
