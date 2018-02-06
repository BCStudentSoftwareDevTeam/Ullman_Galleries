from . import public
from app.logic.validation import *
from flask import render_template
from app.config.loadConfig import get_cfg
import bleach

@public.route('/homepage', methods=["GET","POST"])
def homepage():

    config = get_cfg()
    project_name = config['project_name']
    project_description = config['project_description']
    galleries = GalleryQueries.get_all_open_galleries()
    print(list(galleries))
    return render_template('views/public/gallery_homepage.html', bleach=bleach, galleries = galleries, project_name=project_name, project_description=project_description)




