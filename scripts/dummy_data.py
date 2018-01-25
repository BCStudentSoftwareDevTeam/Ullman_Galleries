import glob,os,sys

path = os.getcwd()
test_dir = os.path.join(path,'app/config/')

if os.path.isdir(test_dir):
    sys.path.insert(0,path)
else:
    new_path = os.path.dirname(path)
    sys.path.insert(0,new_path)

from app.models import *


def load_dummy():

    Users(uid=1, username="adminUser").save(force_insert=True)
    Files(fid=1, filetype="pdf", form=1, filename="Seth's CV", filepath="applications/gallery_1/seth@seth.com/").save(force_insert=True)

    Galleries(gid=1, title="gallery_1", open_date="2001-01-22-11:22", close_date="2018-02-23-11:22", description="HI THIS IS A TEST", banner=1).save(force_insert=True)

    Forms(fid=1, first_name="seth", last_name="roger", street_address="101 Seth Roger Road", city="Blueburge", state="KY", email="seth@seth.com",phone_number="1234567890", website="seth.com", gallery=1, cv=1,personal_statement=1).save(force_insert=True)

    Images(iid=1, form=1, fullsize=1, thumbnail=1).save(force_insert=True)



if __name__ == "__main__":
    models = [Images, Forms, Galleries,Files,Users] 
    database = getDB()
    for model in models:
        database.drop_table(model)

    models = [Users, Files,Galleries,Forms,Images] 
    for model in models:
        model.create_table()
    load_dummy()


