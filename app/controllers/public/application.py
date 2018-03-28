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


@public.route('/application/statement/', methods=["GET"])
def application_statement():
    gid = 1
    if "form_id" not in session or session['form_id'] is None:
        return redirect("/")
    gallery = Galleries.get(Galleries.gid == gid)
    fid = session["form_id"]
    accepted_files = get_cfg()["document_extensions"]
    accepted_files = "." + ",.".join(accepted_files)
    new_files_message = "Please upload your artistic statement"
    existing_files_message = "You previous uploaded the following artistic statement"
    form = Forms.get(Forms.fid == fid)
    pre_exist = False
    if form.personal_statement is not None:
        pre_exist = True

    button_text = "Your Artistic Statement"
    filepath = "/download/statement"
    action = "/upload/statement/"
    next_href = "/application/image/"
    prev_href = "/application/cv/"
    maxFiles = 1
    remove_url = "/delete/statement"
    step = 3
    return render_template(
        'views/public/file_uploads.html',
        next_href=next_href,
        prev_href=prev_href,
        step=step,
        new_files_message=new_files_message,
        existing_files_message=existing_files_message,
        pre_exist=pre_exist,
        maxFiles=maxFiles,
        action=action,
        accepted_files=accepted_files,
        gallery=gallery,
        button_text=button_text,
        filepath=filepath,
        remove_url=remove_url)


@public.route('/application/image/', methods=["GET"])
def application_image():
    gid = 1
    if "form_id" not in session or session['form_id'] is None:
        return redirect("/")
    fid = session["form_id"]
    gallery = Galleries.get(Galleries.gid == gid)
    accepted_files = get_cfg()["allowed_extensions"]
    accepted_files = "." + ",.".join(accepted_files)

    new_files_message = "Please upload your images"
    existing_files_message = "You previous uploaded the following images"
    form = Forms.get(Forms.fid == fid)
    pre_exist = False
    files = FormToFileQueries.get_form_files(fid)

    if files is not None:
        pre_exist = True

    action = "/upload/image/"
    next_href = "/application/review/"
    prev_href = "/application/statement/"
    maxFiles = 40
    step = 4

    allowed_extensions = get_cfg()['allowed_extensions']
    document_extensions = get_cfg()['document_extensions']
    next_button = "Review Application"

    return render_template(
        'views/public/file_uploads.html',
        next_href=next_href,
        prev_href=prev_href,
        step=step,
        new_files_message=new_files_message,
        existing_files_message=existing_files_message,
        pre_exist=pre_exist,
        maxFiles=maxFiles,
        action=action,
        accepted_files=accepted_files,
        gallery=gallery,
        files=files,
        allowed_extensions=allowed_extensions,
        document_extensions=document_extensions,
        next_button=next_button)


@public.route('/application/cv/', methods=["GET"])
def application_cv():
    gid = 1
    if "form_id" not in session or session['form_id'] is None:
        return redirect("/")
    fid = session["form_id"]
    gallery = Galleries.get(Galleries.gid == gid)
    accepted_files = get_cfg()["document_extensions"]
    accepted_files = "." + ",.".join(accepted_files)

    new_files_message = "Please upload your curriculum vitae"
    existing_files_message = "You previous uploaded the following curriculum vitae"
    form = Forms.get(Forms.fid == fid)
    pre_exist = False
    if form.cv is not None:
        pre_exist = True

    button_text = "Your Curriculum Vitae"
    filepath = "/download/cv/"
    action = "/upload/cv/"
    next_href = "/application/statement/"
    prev_href = "/?active_session='true'"
    maxFiles = 1
    remove_url = "/delete/cv"
    step = 2
    return render_template(
        'views/public/file_uploads.html',
        next_href=next_href,
        prev_href=prev_href,
        step=step,
        new_files_message=new_files_message,
        existing_files_message=existing_files_message,
        pre_exist=pre_exist,
        maxFiles=maxFiles,
        action=action,
        accepted_files=accepted_files,
        gallery=gallery,
        button_text=button_text,
        filepath=filepath,
        remove_url=remove_url)


@public.route('/application/personal/', methods=["POST"])
def application_submit():
    gid = 1
    # retrieve the specific gallery for which the application was submitted
    gallery = Galleries.get(Galleries.gid == gid)

    # retrieve data from the form
    data = request.form

    submit_date = time.strftime("%Y-%m-%d %H:%M:%S")

    status = "Pending"

    submission = None
    username = secure_filename(data['firstName'] + '-' + data['lastName'])

    try:
        # Insert data into database
        submission = FormQueries.insert(
            data['firstName'], data['lastName'], data['streetAddress'],
            data['addressLine2'], data['city'], data['stateProvinceRegion'],
            data['zipPostalCode'], data['email'], data['phone'],
            data['website'], gallery, None, None, submit_date, status, None)
    except Exception as e:
        flash("We were unable to process your application")
        return render_template(
            'views/public/personal_info.html', gid=gid,
            gallery=gallery), 500

    # redirect to uploads
    if submission is not None:
        session['form_id'] = submission.fid
        session['username'] = secure_filename(data['firstName'] + '-' + data['lastName'])
        return redirect("/application/cv/")
    else:
        flash("We were unable to process your application")
        return render_template(
            'views/public/personal_info.html', gid=gid,
            gallery=gallery), 500


@public.route('/application/review/', methods=["GET", "POST"])
def review():
    gid = 1
    fid = session['form_id']
    if fid is None:
        return redirect("/")

    form = FormQueries.get(fid)

    files = FormToFileQueries.get_form_files(fid)

    show_next = False
    show_previous = False
    if FormQueries.exists(fid + 1):
        show_next = True
    if FormQueries.exists(fid - 1):
        show_previous = True

    cfg = get_cfg()

    return render_template(
        'views/public/review.html',
        form=form,
        files=files,
        allowed_extensions=cfg['allowed_extensions'],
        document_extensions=cfg['document_extensions'],
        show_next=show_next,
        show_previous=show_previous)
