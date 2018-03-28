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


@admin.route('/users/add', methods=["POST"])
@login_required
def add_user():
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
    role = request.form['role']

    if password == confirm:
        datastore = current_app.extensions['security'].datastore
        if datastore.get_user(email) is not None:
            flash("User %s already exists" % (email), "danger")
        else:
            if role != "student":
                if current_user.has_role("admin"):
                    role = datastore.find_role("admin")
                    user = datastore.create_user(
                        email=email, password=hash_password(password))
                    datastore.add_role_to_user(user, role)
                    flash("User %s has been created" % (email), "success")
                else:
                    flash("Only admins can add non-student users", "danger")
            else:
                role = datastore.find_role("student")
                user = datastore.create_user(
                    email=email, password=hash_password(password))
                datastore.add_role_to_user(user, role)
                flash("User %s has been created" % (email), "success")
    else:
        flash("Passwords do not match", "danger")
    return redirect("/view")


@admin.route('/users/remove', methods=["POST"])
@login_required
def remove_user():
    datastore = current_app.extensions['security'].datastore
    email = request.form['email']
    user = datastore.get_user(email)
    if user.has_role("admin"):
        if current_user.has_role("admin"):
            datastore.delete_user(user)
            flash("User %s has been removed" % (email), "success")
        else:
            flash("User %s can only be removed by an admin" % (email),
                  "danger")
    else:
        datastore.delete_user(user)
        flash("User %s has been removed" % (email), "success")
    return redirect("/view")


@admin.route('/users/change_password', methods=["POST"])
@login_required
def change_password():
    password = request.form['password']
    confirm = request.form['confirm']
    current = request.form['current']

    if password == confirm:
        user_id = session["user_id"]
        datastore = current_app.extensions['security'].datastore
        user = datastore.get_user(user_id)
        verify = verify_password(current, user.password)
        if verify:
            user.password = hash_password(password)
            user.save()
            flash("Your password has been updated", "success")
        else:
            flash("The password supplied was incorrect", "danger")
        return redirect("/view/")
    else:
        flash("Passwords must match", "danger")
        return redirect("/view/")
