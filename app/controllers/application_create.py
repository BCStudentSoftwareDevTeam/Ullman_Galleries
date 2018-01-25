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



@app.route('/application/submit/<gid>', methods=["GET", "POST"])
def application_submit(gid):
    gallery = Galleries.get(Galleries.gid==gid)
    application_obj = FormQueries()
     
    data        = request.form
    submit_date = time.strftime("%m%d%y")
    
    try:
        #Insert data into database
        submission =  application_obj.insert(data['firstName'],
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
      
        try:
            # save uploads in the database with the associated FID
            fid = submission.fid
            if 'cv' in request.files:
                cv = request.files['cv']
                cv_ext    = (str(cv.filename.split(".").pop())).replace(" ","")
                cv_filename = "cv_{}".format(data['firstName']+ '_'+ data['lastName'])
                cv_upload_path = getAbsolutePath(cfg['paths']['files'],cv_filename,True)
                cv.save(cv_upload_path)
                application_obj.insert_cv_file(fid,cv_filename,cv_upload_path,cv_ext)
            
            if 'statement' in request.files:   
                statement = request.files['statement']
                statement_ext    = (str(statement.filename.split(".").pop())).replace(" ","")
                statement_filename = "personal_statement_{}".format(data['firstName']+ '_'+ data['lastName'])
                statement_upload_path = getAbsolutePath(cfg['paths']['files'],statement_filename)
                # statement.save(statement_upload_path)
                application_obj.insert_statement_file(fid,statement_filename,statement_upload_path,statement_ext)
                    
            flash("Your application was successfully submitted.")
            return render_template('views/application_review.html',gid=gid, gallery = gallery, cfg=cfg)

        except Exception as e:
            print (e)
            flash("An error occured while saving uploaded files.")
            return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)

    else:
        flash("Your application was not submitted, for an error occured in the process.")
        return render_template('views/application_create.html',gid=gid, gallery = gallery, cfg=cfg)