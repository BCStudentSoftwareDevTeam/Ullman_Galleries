from flask import Blueprint

admin = Blueprint('administrator', __name__)

from . import all_galleries
from . import gallery_edit
from . import gallery_submission
from . import gallery_view
