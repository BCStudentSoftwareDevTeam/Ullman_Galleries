from flask import Blueprint
public = Blueprint('public', __name__)

from . import application_create
from . import application_review