from flask import Blueprint

admin = Blueprint('administrator', __name__)

from . import base
from . import delete
from . import download
from . import users
from . import view
