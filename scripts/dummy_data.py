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
    load_user_data()
    load_role_data()
    load_userroles_data()
    # load_files_data()
    load_galleries_data()
    # load_forms_data()
    # load_images_data()


def load_user_data():
    Users(email="heggens@berea.edu", password="heggens@berea.edu").save(force_insert=True)
    Users(email="sotoventuraj@berea.edu", password="sotoventuraj@berea.edu").save(force_insert=True)

def load_role_data():
    Role(name="admin").save(force_insert=True)
    Role(name="student").save(force_insert=True)

def load_userroles_data():
    UserRoles(user=1, role=1).save(force_insert=True)
    UserRoles(user=2, role=2).save(force_insert=True)


def load_galleries_data():
    Galleries(gid=1, title="Doris Ulmann  Gallery",  folder_name="/static/data/D. Ulmann Gallery/").save(force_insert=True)

def load_files_data():
    pass
def load_forms_data():
    pass
def load_images_data():
    pass
if __name__ == "__main__":
    dummy_data()

