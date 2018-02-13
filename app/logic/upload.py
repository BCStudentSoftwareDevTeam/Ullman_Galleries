# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from app.models import *
from app.models.queries import *
from app.logic.absolute_path import *
from flask import request
from werkzeug.utils import secure_filename
import os, re, datetime

cfg = get_cfg()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in cfg['allowed_extensions']


def upload(request, absolute_path):
    if 'file' not in request.files:
            print ('No file part')
            return None # maybe replace with raising exception
    
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        print('No selected file')
        return None # maybe replace with raising exception
    
    if file and allowed_file(file.filename):
        file.save(absolute_path)
        return absolute_path


def get_app_path(relativePath):
    return cfg['paths']['app'] + relativePath

def new_gallery_path(title):
    now = datetime.datetime.now()
    relativePath = '{0}/{1}_{2}_{3}_{4}'.format(cfg['paths']['data'], title, now.year, now.month, now.day)
    
    dirpath = os.path.join(sys.path[0],get_app_path(relativePath))
    # create the gallery folder if it does not exist
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
    
    return '{0}/banner.jpg'.format(relativePath) #TODO: figure out how to rename files better way

    
    
def gallery_banner_upload(request, title, fid=None):

    if fid:
        file = FilesQueries.get(fid)
        relativePath = get_app_path(file.filepath) 
        
    else:
        file = request.files['file']
        filename = secure_filename(file.filename)
        staticPath = new_gallery_path(title)
        fid = FilesQueries.insert(staticPath, filename, 'jpg') #TODO: raise error if fid is not returned
        relativePath = get_app_path(staticPath)
    
    absolute_path = getAbsolutePath(relativePath)
    upload_path = upload(request, absolute_path)
    
    if upload_path is not None:
        return fid


def create_form_path(galleryFolderName, email):
    
    dirpath = os.path.join(sys.path[0])
    # create the gallery folder if it does not exist
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
