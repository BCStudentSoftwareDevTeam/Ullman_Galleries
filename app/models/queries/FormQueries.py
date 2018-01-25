from app.models import Forms
from app.models import Files

class FormQueries():
    def select_all(self):
        try:
            forms = Forms.select()
            return forms
        except Exception as e:
            return False
        
    def select_single(self, fid):
        try:
            form = Forms.get(Form.fid == fid)
            return form
        except Exception as e:
            print (e) 
            return False
            
    def select_from_list(self, listFID):
        try:
            form = Forms.select().where(Forms.fid << listFID)
            return form
        except Exception as e:
            print (e) 
            return False

    def insert(self,first_name, last_name, street_address, second_address,city, state, zipCode, email, phone_number, website, gallery,cv, personal_statement, submit_date ):
        # strings=[first_name, last_name, street_address, second_address,city, state, email, phone_number, website, gallery,cv, personal_statement, submit_date]
        # if checkStrings(strings) & self.validateEmail(email):
        try:
            form = Forms(first_name=first_name, last_name=last_name, street_address=street_address, second_address=second_address,city=city, state=state,zipCode = zipCode, email=email, phone_number=phone_number, website=website, gallery=gallery,cv=cv, personal_statement=personal_statement, submit_date=submit_date)
            form.save()
            return form
        except Exception as e:
            return e
        return False
        
    def insert_cv_file(self,fid, filename, filepath, filetype):
        try: 
            form = Forms.get(Forms.fid == fid)
            cv = Files(filepath = filepath, filename=filename, filetype = filetype)
            cv.save()
            form.cv = cv
            form.save()
            return form
        except Exception as e:
            print (e)
            return False
          
    def insert_statement_file(self, fid, filename, filepath, filetype):
        try:
            form = Forms.get(Forms.fid == fid)
            personal_statement = Files(filepath = filepath, filename=filename, filetype = filetype)
            personal_statement.save()
            form.personal_statement = personal_statement
            form.save()
            return form
        except Exception as e:
            print (e)
            return False

   