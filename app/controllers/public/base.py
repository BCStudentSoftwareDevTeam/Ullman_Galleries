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
from app.controllers.public.status import change_status
import shutil


@public.route('/', methods=["GET"])
def create():
    if not doesUserHaveRole('anonymous'):
        return redirect('/view')
    form = None
    show_clear = True
    if 'form_id' not in session or ('submitted' in session
                                    and session['submitted']):
        session['form_id'] = None
        session['username'] = None
        session['submitted'] = False
        show_clear = False
    if session['form_id'] is not None:
        fid = session["form_id"]
        form = FormQueries.get(fid)
        if "active_session" in request.args:
            show_clear = False
    else:
        show_clear = False
    gid = 1
    gallery = Galleries.get(Galleries.gid == gid)
    description = gallery.description
    return render_template(
        'views/public/personal_info.html',
        gid=gid,
        description=description,
        gallery=gallery,
        form=form,
        show_clear=show_clear)


@public.route("/contributors/")
def contributors():
    return render_template("snips/contributors.html", cfg=get_cfg())


@public.route('/withdraw/', methods=["GET"])
def withdraw():
    change_status('withdraw')
    session['form_id'] = None
    session['user_name'] = None
    return redirect('/')


@public.route('/success/', methods=["GET", "POST"])
def success():
    fid = session['form_id']
    session['submitted'] = True
    if fid is None:
        flash("Unable to complete your application", "danger")
        return redirect("/")
    else:
        form = FormQueries.get(fid)
        form.status = "Completed"
        form.save()
        session['form_id'] = None
        session['user_name'] = None
        return render_template('views/public/success.html')
