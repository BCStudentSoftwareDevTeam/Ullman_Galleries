from app.models import Forms
from app.models import Files



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


def select_single(self, fid):
    '''This method is to select a single form from the database using the unique identifier (FID) associated with that form'''
    try:
        form = Forms.get(Form.fid == fid)
        return form
    except Exception as e:
        print (e)
        return False

def insert(self,first_name, last_name, street_address, second_address,city, state, zip_code, email, phone_number, website, gallery,cv, personal_statement, submit_date ):
    '''This method is to store the inputs received from the application form into the database'''
    try:
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
                        submit_date=submit_date
                    )
        form.save()
        return form
    except Exception as e:
        return e
    return False

def insert_attachment_file(self,doc_type, fid, filename, filepath, filetype):
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
