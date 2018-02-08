from app.models import Forms
from app.models import Files
from app.models import Galleries

def get(fid):
    """ Retrieves a single form object

    Args:
        fid (int): The fid of the form model to retrieve 

    Returns:
        Form: The gallery object if it exists
        None: If the form object does not exist
    """

    if type(fid) is int:
        if Forms.select().where(Forms.fid == fid).exists():
            return Forms.get(Forms.fid == fid)
    return None

def get_all_from_gallery(gid):
    """ Retrieves all form object for a single gallery

    Args:
        gid (int): The gid of the gallery model to retrieve forms from

    Returns:
        Forms (list): A list of the form objects for a gallery
        None: If the gallery object does not exist
    """

    if type(gid) is int:
        if Galleries.select().where(Galleries.gid == gid).exists():
            forms = Forms.select().join(Galleries).where(Galleries.gid == gid)
            return list(forms)
    return None



def get(fid):
    """ Retrieves a single Form object

    Args:
        fid (int): The fid of the Form model to retrieve 

    Returns:
        Form: The Form object if it exists
        None: If the Form object does not exist
    """

    if type(fid) is int:
        if Forms.select().where(Forms.fid == fid).exists():
            return Forms.get(Forms.fid == fid)
    return None

def select_all(self):
    '''This method is to select all the forms stored in the database'''
    try:
        forms = Forms.select()
        return forms
    except Exception as e:
        print (e)
        return False


def select_single(fid):
    '''This function is to select a single form from the database using the unique identifier (FID) associated with that form'''
    try:
        form = Forms.get(Form.fid == fid)
        return form
    except Exception as e:
        print (e)
        return False

def insert(first_name, last_name, street_address, second_address,city, state, zip_code, email, phone_number, website, gallery,cv, personal_statement, submit_date, status):
    '''This function is to store the inputs received from the application form into the database'''
    try:
        print("Saving:FormQueries")
        form = Forms(   first_name=first_name,
                        last_name=last_name,
                        street_address=street_address,
                        second_address=second_address,
                        city=city,
                        state=state,
                        zip_code=zip_code,
                        email=email,
                        phone_number=phone_number,
                        website=website,
                        gallery=gallery,
                        cv=cv,
                        personal_statement=personal_statement,
                        submit_date=submit_date,
                        status=status
                    )
        print("Saved: FormQueries")
        form.save()
        return form
    except Exception as e:
        return e
    return False

def insert_attachment_file(doc_type, fid, filename, filepath, filetype):
    '''This method is to store attachment files such as CVs and personal statements into the database'''
    form = Forms.get(Forms.fid == fid)
    file = Files(filepath = filepath, filename=filename, filetype = filetype)
    file.save()
    if doc_type == "cv":
        try:
            form.cv = file
        except Exception as e:
            print (e)
            return False
    if doc_type =="statement":
        try:
            form.personal_statement = file
        except Exception as e:
            print (e)
            return False
    form.save()
    return form
    
def get_image_info(number,im_type, file_ext):
    cfg = get_cfg()
    if im_type == "fullsize":
        filename = "image_{}".format(number)+"."+file_ext
    elif im_type == "thumbnail":
        filename = "image_{}_thumb".format(number)+"."+file_ext
    upload_path = getAbsolutePath(cfg['paths']['app']+cfg['paths']['data']+"/"+gallery_folder+"/"+submission_folder,filename)
    if os.path.isfile(upload_path):
        number += 1
        return get_file_info(number,cfg, im_type, file_ext)
    else:
        return filename
