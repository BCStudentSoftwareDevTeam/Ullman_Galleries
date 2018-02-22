from flask import Blueprint

admin = Blueprint('administrator', __name__)

from . import gallery_view

