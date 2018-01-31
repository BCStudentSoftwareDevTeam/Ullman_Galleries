# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from app.models import *
from app.logic.absolute_path import *
from flask import request
from werkzeug.utils import secure_filename
import os, re, datetime

cfg = get_cfg()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in cfg['allowed_extensions']


def upload(request, relativePath):
    try:
        if 'file' not in request.files:
                print ('No file part')
                return None # maybe replace with raising exception
        file = request.files['file']
        print (file.filename)
        
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return None # maybe replace with raising exception
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            absolute_path = getAbsolutePath(rerlativePath, filename)
            file.save(absolute_path)
            return absolute_path
            
    except Exception as e:
        print(e)
    
    return None
    
    
def gallery_banner_upload(request, galleryTitle):
    # now = datetime.datetime.now()
    relativePath = cfg['paths']['files']+'/'+ galleryTitle
    filepath = os.path.join(sys.path[0],relaitivePath)
    
    # create the gallery folder if it does not exist
    if not os.path.isdir(filepath):
        os.makedirs(filepath)
    
    return upload(request, relativePath)