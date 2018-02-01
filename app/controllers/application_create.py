from app.allImports import *
from app.logic.validation import *
from app.models.queries.FormQueries import FormQueries
from werkzeug.security import check_password_hash
from flask import session
import os, sys
import time


@app.route('/application/create/<gid>', methods=["GET","POST"])
def create(gid):
    gallery = Galleries.get(Galleries.gid==gid)
    return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)

def get_image_info(number,cfg,im_type, file_ext):
    if im_type == "fullsize":
        filename = "image_{}".format(number)
    elif im_type == "thumbnail":
        filename = "image_{}_thumb".format(number) 
    upload_path = getAbsolutePath(cfg['paths']['files'],filename)
    if os.path.isfile(upload_path):
        number = number+1
        return get_file_info(number,cfg, im_type, file_ext)
    else:
        return filename

@app.route('/application/submit/<gid>', methods=["GET", "POST"])
def application_submit(gid):
    # retrieve the specific gallery for which the application was submitted
    gallery         = Galleries.get(Galleries.gid==gid)
    
    # create a Formqueries class object to insert data from the form and attachment files into the database. 
    application_obj = FormQueries()
     
    # retrieve data from the form
    data            = request.form
    
    submit_date     = time.strftime("%m/%d/%y %H:%M:%S")
  
    try:
        #Insert data into database
        submission   =  application_obj.insert(data['firstName'],
                                             data['lastName'],
                                             data['streetAddress'],
                                             data['addressLine2'],
                                             data['city'],
                                             data['stateProvinceRegion'],
                                             data['zipPostalCode'],
                                             data['email'],
                                             data['phone'],
                                             data['website'],
                                             gallery,
                                             None,
                                             None,
                                             submit_date)
    except Exception as e:
        print (e)
        flash ("An error occured during submission.")
        return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)

        
    if submission != False:
        # save uploads in the database with the associated FID
        fid  = submission.fid
        try:
            
            if 'cv' in request.files:
                # retrieve the cv uploaded in the application form
                cv             = request.files['cv']
                
                # store the file extension 
                cv_ext         = (str(cv.filename.split(".").pop())).replace(" ","")
                
                # rename the file uploaded to a specific format
                cv_filename    = "cv_{}".format(data['firstName']+ '_'+ data['lastName'])
                
                # store the absolute path where the file will be stored on the server
                cv_upload_path = getAbsolutePath(cfg['paths']['files'],cv_filename,True)
                
                # save the file on the server
                cv.save(cv_upload_path)
                
                # save the file in the database in the Files table
                application_obj.insert_attachment_file("cv", fid,cv_filename,cv_upload_path,cv_ext)
        
        except Exception as e:
            print (e)
        
            flash("An error occured while saving cv file!")
        
            return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)
        
        try:    
        
            if 'statement' in request.files:   
                # retrieve the personal statement uploaded in the application form 
                statement             = request.files['statement']
                
                # store the file extension 
                statement_ext         = (str(statement.filename.split(".").pop())).replace(" ","")
                
                # rename the file uploaded to a specific format
                statement_filename    = "personal_statement_{}".format(data['firstName']+ '_'+ data['lastName'])
                
                # store the absolute path where the file will be stored on the server
                statement_upload_path = getAbsolutePath(cfg['paths']['files'],statement_filename,True)
                
                # save the file on the server
                statement.save(statement_upload_path)
                
                # save the file in the database in the Files table
                application_obj.insert_attachment_file("statement", fid,statement_filename,statement_upload_path,statement_ext)
        
        except Exception as e:
            print (e)
        
            flash("An error occured while saving the personal statement file!")
        
            return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)
          
        try:
            number = 1
            try:
                images = request.files['images']
                print("It is working!")
            except Exception as e:
                print("There is a problem with request file")
            # file_ext    = (str(images.filename.split(".").pop())).replace(" ","")
            # im_filename = get_image_info(number, cfg, "fullsize", file_ext)
            # im_upload_path = getAbsolutePath(cfg['paths']['files'],im_filename,True)
            # images.save(im_upload_path)
            # file = Files(filepath = im_upload_path, filename = im_filename, filetype = file_ext)
            # im = Images(form = fid, fullsize = im_filename, thumbnail = None )
        except Exception as e:
            print (e)
            print("I messed up!")
            
        flash("Your application was successfully submitted.")
 
        return render_template('views/application_review.html',gid=gid, gallery = gallery, cfg=cfg)

    else:
        flash("Your application was not submitted, for an error occured in the process.")
 
    return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)
 
