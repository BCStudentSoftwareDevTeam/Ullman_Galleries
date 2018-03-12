import glob,os,sys

path = os.getcwd()
test_dir = os.path.join(path,'app/config/')

if os.path.isdir(test_dir):
    sys.path.insert(0,path)
else:
    new_path = os.path.dirname(path)
    sys.path.insert(0,new_path)

from app.models import *

def drop_tables():
    models = [FormToFile, UserRoles, Forms, Galleries,Files,Users, Role] 
    for model in models:
        if model.table_exists():
            model.drop_table()

def create_tables():
    models = [Users, Role, Files,Galleries,Forms,FormToFile,UserRoles] 
    for model in models:
        if not model.table_exists():
            model.create_table()

def dummy_data():
    drop_tables()
    create_tables()
    # load_user_data()
    # load_files_data()
    load_galleries_data()
    # load_forms_data()
    # load_images_data()

def load_user_data():
    Users(uid=1, username="adminUser").save(force_insert=True)

def load_galleries_data():
    Galleries(gid=1, title="D. Ullman Gallery", folder_name = "D. Ullman Gallery").save(force_insert=True)

def load_files_data():
    pass
def load_forms_data():
    pass
def load_images_data():
    pass
if __name__ == "__main__":
    dummy_data()

