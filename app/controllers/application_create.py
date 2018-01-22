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


@app.route('/application/submit/<gallery>', methods=["GET", "POST"])
def application_submit(gallery):
    
 
     
    data        = request.form
    # submit_date = time.strftime("%m%d%y")
    
    # try:
    #     #Insert data into database
    #     submission =  application_obj.insert(data['firstName'],
    #                                          data['lastName'],
    #                                          data['streetAddress'],
    #                                          data['city'],
    #                                          data['stateProvinceRegion'],
    #                                          data['zipPostalCode'],
    #                                          data['email'],
    #                                          data['phone'],
    #                                          data['website'],
    #                                          None,
    #                                          None,
    #                                          None)
    # except Exception as e:
    #     print (e)
    #     flash ("An error occured during submission.")
    #     return redirect(url_for("/application/create/<gid>"))
        
    # if submission != False:
    #     try:
    #         # save uploads in the database with the associated FID
    #         FID = submission.fid
    #         data_val_obj = DataValidation()
    #         application = Forms.get(Forms.fid == FID)
            
    #         cv = request.files['cv']
    #         cv_ext    = (str(cv.filename.split(".").pop())).replace(" ","")
    #         cv_filename = "cv_{}".format(data['firstName']+ '_'+ data['lastName']) + '.' + file_ext
    #         cv_upload_path = getAbsolutePath(cfg['paths']['files'],cv_filename,True)
    #         cv.save(cv_upload_path)
            
    #         application.cv.filename = cv_filename
    #         application.cv.filetype = cv_ext
    #         application.cv.filepath = cv_upload_path
            
    #         statement = request.files['statement']
    #         statement_ext    = (str(statement.filename.split(".").pop())).replace(" ","")
    #         statement_filename = "statement_{}".format(data['firstName']+ '_'+ data['lastName']) + '.' + file_ext
    #         statement_upload_path = getAbsolutePath(cfg['paths']['files'],statement_filename,True)
    #         statement.save(statement_upload_path)
            
    #         application.personal_statement.filename = statement_filename
    #         application.personal_statement.filetype = statement_ext
    #         application.personal_statement.filepath = statement_upload_path
            
    #         # letter      = chr(ord('a'))
    #         # images = request.files['fileDropZone']
    #         # file_ext    = (str(images.filename.split(".").pop())).replace(" ","")
    #         # im_filename = get_image_info(letter, file_ext, fid, cfg, "fullsize")
    #         # im_upload_path = getAbsolutePath(cfg['paths']['files'],im_filename)
    #         # images.save(im_upload_path)
            
    #         # # https://stackoverflow.com/questions/2612436/create-thumbnail-images-for-jpegs-with-python
            
    #         # thumbnail_size = 128,128
    #         # try:
    #         #     im_thumbnail = images.thumbnail(thumbnail_size)
    #         #     filename = get_image_info(letter, file_ext, fid, cfg, "thumbnail")
    #         #     imT_upload_path = getAbsolutePath(cfg['paths']['files'],filename)
    #         #     im_thumbnail.save(imT_upload_path)
    #         # except Exception as e:
    #         #     print("Thumbnail cannot be created!")
    #         #     print (e)
            
    #         # application.images.fullsize = images
    #         # appliation.images.thumbnail = im_thumbnail
    #         appliation.save()
    #         flash("Your application was successfully submitted.")
    #         return redirect(url_for("/"))
    
    #     except Exception as e:
    #         print (e)
    #         flash("An error occured while saving uploaded files.")
    #         return redirect(url_for("/application/create/<gid>"))
    # else:
    #     flash("Your application was not submitted, for an error occured in the process.")
    #     return redirect(url_for("/application/create/<gid>"))
    
        
        

