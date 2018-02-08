from . import public
from flask import render_template, g
from app.logic.validation import*
from app.models.queries.FormQueries import*
from app.config.loadConfig import get_cfg
from flask import session
from flask import current_app
import os, sys
import time



@public.route('/application/create/<gid>', methods=["GET"])
def create(gid):
    gallery = Galleries.get(Galleries.gid==gid)
    return render_template('views/public/application_create.html',gid=gid, gallery = gallery)


@public.route('/application/submit/<gid>', methods=["POST"])
def application_submit(gid):
    # retrieve the specific gallery for which the application was submitted
    gallery         = Galleries.get(Galleries.gid==gid)
    
    # retrieve data from the form
    data            = request.form

    submit_date     = time.strftime("%m/%d/%y %H:%M:%S")
    
    status          = "Pending"

    try:
        #Insert data into database
        submission  = FormQueries.insert(   data['firstName'],
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
                                            submit_date,
                                            status
                                        )
       
    except Exception as e:
        print (e)
        flash ("An error occured during submission.")
        return render_template('views/public/application_create.html',gid=gid, gallery = gallery)

    print("Done inserting into the database!")
    if submission != False:
        cfg = get_cfg() 
        # save uploads in the database with the associated FID
        fid  = submission.fid
        
        gallery_folder = str(gallery.folder_name)
        submission_folder = data['email']
        try:

            if 'cv' in request.files:
                # retrieve the cv uploaded in the application form
                cv             = request.files['cv']

                # store the file extension
                cv_ext         = (str(cv.filename.split(".").pop())).replace(" ","")

                # rename the file uploaded to a specific format
                cv_filename    = "cv_{}".format(data['firstName']+ '_'+ data['lastName']) + '.' + cv_ext

                # get the absolute path where the file will be stored on the server
                cv_upload_path = getAbsolutePath(cfg['paths']['app']+cfg['paths']['data']+"/"+gallery_folder+"/"+submission_folder,cv_filename,True)
  
                # save the file on the server
                cv.save(cv_upload_path)
                # save the file in the database in the Files table
                saved_cv = FormQueries.insert_attachment_file("cv", fid,cv_filename,cv_upload_path,cv_ext)
                print("Cv saved!")
        except Exception as e:
            print (e)

            flash("An error occured while saving cv file!")

            return render_template('views/public/application_create.html',gid=gid, gallery = gallery)

        try:

            if 'statement' in request.files:
                # retrieve the personal statement uploaded in the application form
                statement             = request.files['statement']

                # store the file extension
                statement_ext         = (str(statement.filename.split(".").pop())).replace(" ","")

                # rename the file uploaded to a specific format
                statement_filename    = "personal_statement_{}".format(data['firstName']+ '_'+ data['lastName'])

                # get the absolute path where the file will be stored on the server
                statement_upload_path = getAbsolutePath(cfg['paths']['app']+cfg['paths']['data']+"/"+gallery_folder+"/"+submission_folder,statement_filename,True)
               
                # save the file on the server
                statement.save(statement_upload_path)

                # save the file in the database in the Files table
                saved_statement = FormQueries.insert_attachment_file("statement", fid,statement_filename,statement_upload_path,statement_ext)
          
        except Exception as e:
            print (e)

            flash("An error occured while saving the personal statement file!")

            return render_template('views/public/application_create.html',gid=gid, gallery = gallery)
        
         #redirect to uploads
        url = 'upload/{}'.format(fid)
        return redirect(url)

    else:
        flash("Your application was not submitted, for an error occured in the process.")

    return render_template('views/public/application_create.html',gid=gid, gallery = gallery)


@public.route('/upload/<fid>', methods=["GET"])
def upload(fid):
    return render_template('snips/upload.html', fid = fid)
    
    
    
@public.route('upload/images/<fid>', methods = ["GET", "POST"])
def upload_images(fid):
    
    form = FormQueries.get(fid)
    images = request.files['file']
    file_ext    = (str(images.filename.split(".").pop())).replace(" ","")
    im_filename = get_image_info(number, cfg, "fullsize", file_ext)
    im_upload_path = getAbsolutePath(cfg['paths']['app']+cfg['paths']['data']+"/"+gallery_folder+"/"+submission_folder,im_filename,True)
    images.save(im_upload_path)
    file = Files(filepath = im_upload_path, filename = im_filename, filetype = file_ext)
    im = Images(form = fid, fullsize = file, thumbnail = None )
    
    flash("Your application was successfully submitted.")
    return render_template('views/public/application_review.html',form = form)
        

