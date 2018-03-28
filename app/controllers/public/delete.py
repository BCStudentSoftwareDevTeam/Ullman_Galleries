from . import public
from flask import render_template, g
from app.logic.validation import *
from app.models.queries.FormQueries import *
from app.models.queries.FilesQueries import *
from app.logic.upload import *
from app.config.loadConfig import get_cfg
from flask import session
from flask import current_app
from app.models.queries.FormToFileQueries import *
from datetime import datetime
import os
import sys
import time
import io
import bleach
import json


@public.route("/delete/image", methods=["POST"])
def delete_image():
    try:
        fid = session['form_id']
        filepath = request.form['filepath']
        FormToFileQueries.delete_file(fid, filepath)
    except Exception as error:
        return "Unable to delete", 500
    else:

        return "200", 200


@public.route("/delete/cv", methods=["POST"])
def delete_cv():
    try:
        fid = session['form_id']
        filepath = request.form['filepath']
        form = FormQueries.get(fid)
        FormToFileQueries.delete_file(fid, filepath)
        form.cv = None
        form.save()
    except Exception as error:
        return "Unable to delete", 500
    else:
        return "200", 200


@public.route("/delete/statement", methods=["POST"])
def delete_statement():
    try:
        fid = session['form_id']
        filepath = request.form['filepath']
        form = FormQueries.get(fid)
        FormToFileQueries.delete_file(fid, filepath)
        form.personal_statement = None
        form.save()
    except Exception as error:
        return "Unable to delete", 500
    else:
        return "200", 200
