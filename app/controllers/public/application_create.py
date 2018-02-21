from . import public
from flask import render_template, g
from app.logic.validation import*
from app.models.queries.FormQueries import*
from app.models.queries.FilesQueries import*
from app.models.queries.ImageQueries import*
from app.logic.upload import *
from app.config.loadConfig import get_cfg
from flask import session
from flask import current_app
import os, sys
import time
from PIL import Image
import io

import json



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

    if submission != False:
        cfg = get_cfg()
        # save uploads in the database with the associated FID
        fid  = submission.fid
        form = FormQueries.get(fid)
        staticPath = cfg['paths']['data']+"/"+form.gallery.folder_name+"/"+ form.email
        try:

            if 'cv' in request.files:
                # retrieve the cv uploaded in the application form
                cv             = request.files['cv']

                # store the file extension
                cv_ext         = (str(cv.filename.split(".").pop())).replace(" ","")

                # rename the file uploaded to a specific format
                cv_filename    = "cv_{}".format(data['firstName']+ '_'+ data['lastName']) + '.' + cv_ext

                # get the absolute path where the file will be stored on the server
                cv_upload_path = getAbsolutePath(cfg['paths']['app']+staticPath,cv_filename,True)

                # save the file on the server
                cv.save(cv_upload_path)
                # save the file in the database in the Files table
                saved_cv = FormQueries.insert_attachment_file("cv", fid,cv_filename,staticPath+'/'+cv_filename,cv_ext)

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
                statement_filename    = "personal_statement_{}".format(data['firstName']+ '_'+ data['lastName'] +statement_ext )

                # get the absolute path where the file will be stored on the server
                statement_upload_path = getAbsolutePath(cfg['paths']['app']+staticPath,statement_filename,True)

                # save the file on the server
                statement.save(statement_upload_path)

                # save the file in the database in the Files table
                saved_statement = FormQueries.insert_attachment_file("statement", fid,statement_filename,staticPath+'/'+statement_filename,statement_ext)

        except Exception as e:
            print (e)

            flash("An error occured while saving the personal statement file!")

            return render_template('views/public/application_create.html',gid=gid, gallery = gallery)

        # redirect to uploads
        session['form_id'] = fid
        return redirect('upload')


    else:
        flash("Your application was not submitted, for an error occured in the process.")

    return render_template('views/public/application_create.html',gid=gid, gallery = gallery)


@public.route('/upload/', methods=["GET"])
def upload():
    fid = session['form_id']
    if select_single(fid) != None:
        return render_template('snips/upload.html', fid = fid)
    else:
        return render_template('views/404.html')


@public.route('/upload/images/', methods = ["POST"])
def upload_images():
    fid = session['fid']
    try:
        cfg = get_cfg()
        # import pdb;pdb.set_trace()
        form = Forms.get(Forms.fid == fid)
        count = ImageQueries.image_count(form.fid)
        for i, f in enumerate(request.files):
            count += 1
            img = request.files[f]
            file_ext = get_file_extension(img.filename)
            staticPath = cfg['paths']['data']+"/"+form.gallery.folder_name+"/"+ form.email
            new_file_name = "Image"+str(count)+'.'+file_ext
            im_upload_path = getAbsolutePath(cfg['paths']['app']+staticPath, new_file_name, True)

            # Documentation for creating thumbnails: https://www.united-coders.com/christian-harms/image-resizing-tips-every-coder-should-know/
            image_buffer = io.BytesIO(img.read())
            img.seek(0)

            im_thumbnail = Image.open(image_buffer)
            im_thumbnail.thumbnail((200,200), Image.ANTIALIAS)
            thumbnail_file_name = "Image"+str(count)+'_thumb.'+file_ext
            thumbnail_upload_path = getAbsolutePath(cfg['paths']['app']+staticPath, thumbnail_file_name, True)


            if allowed_file(img.filename):
                img_fullsize_id = FilesQueries.insert(staticPath+'/'+new_file_name, new_file_name, file_ext)
                img.save(im_upload_path)
                img_thumbnail_id = FilesQueries.insert(staticPath+'/'+thumbnail_file_name, thumbnail_file_name, file_ext)
                im_thumbnail.save(thumbnail_upload_path)
                iid = ImageQueries.insert(fid, img_fullsize_id,img_thumbnail_id)
        return "Suc"

    except Exception as e:
        print(e)

