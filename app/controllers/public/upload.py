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


@public.route("/upload/statement/", methods=["POST"])
def upload_statement():
    return upload("statement")


@public.route("/upload/cv/", methods=["POST"])
def upload_cv():
    return upload("cv")


@public.route('/upload/image/', methods=["POST", "GET"])
def upload_image():
    return upload("image")


def upload(upload_type):
    fid = session['form_id']
    username = session['username']
    message = "Complete"
    status = 200

    if fid is None or username is None:
        return abort(404)
    try:
        cfg = get_cfg()
        form = Forms.get(Forms.fid == fid)
        staticPath = form.gallery.folder_name + "/" + secure_filename(username) + "-" + str(fid)
        if form.folder_path is None:
            form.folder_path = staticPath
            form.save()
        file_count = FormToFileQueries.file_count(fid)
        print(file_count)
        for i, f in enumerate(request.files):
            file_count += 1
            file = request.files[f]
            file_ext = get_file_extension(file.filename)
            date = str(datetime.today().__format__("%m-%d-%y"))
            if upload_type == "cv":
                new_file_name = date + "-" + username + "-CV"
            elif upload_type == "statement":
                new_file_name = date + "-" + username + "-Statement"
            else:
                new_file_name = date + "-" + username + \
                    "-Image" + "-" + str(file_count)
            new_file_name += "." + file_ext
            new_file_name = secure_filename(new_file_name)

            file_upload_path = getAbsolutePath(
                cfg['paths']['app'] + staticPath, new_file_name, True)

            if allowed_file(file.filename):
                if upload_type == "cv":
                    FormQueries.insert_attachment_file(
                        "cv", fid, new_file_name,
                        staticPath + '/' + new_file_name, file_ext)
                    file.save(file_upload_path)
                elif upload_type == "statement":
                    FormQueries.insert_attachment_file(
                        "statement", fid, new_file_name,
                        staticPath + '/' + new_file_name, file_ext)
                    file.save(file_upload_path)
                else:
                    file_id, created = FilesQueries.insert(
                        staticPath + '/' + new_file_name, new_file_name,
                        file_ext)
                    if created:
                        FormToFileQueries.insert(fid, file_id)
                        file.save(file_upload_path)
                    else:
                        message = "File already exists"
                        status = 501
        return message, status

    except Exception as e:
        return "We were unable to upload the file, please try again", 501
