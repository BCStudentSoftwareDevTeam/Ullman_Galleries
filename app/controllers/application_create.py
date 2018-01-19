from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session
import os, sys
import time


@app.route('/application/create/<gid>', methods=["GET","POST"])
def create(gid):
    gallery = Galleries.get(Galleries.gid==gid)
    return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)

def get_image_info(letter, file_ext, fid, cfg,im_type):
    if im_type == "fullsize":
        filename = "Im_Application_{}".format(fid)+letter + '.' + file_ext
    elif im_type == "thumbnail":
        filename = "ImT_Application_{}".format(fid)+letter + '.' + file_ex
    upload_path = getAbsolutePath(cfg['paths']['files'],filename)
    if os.path.isfile(upload_path):
        letter = chr(ord(letter)+1)
        return get_file_info(letter,file_ext,fid,cfg)
    else:
        return filename