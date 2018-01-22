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
    models = [Images, Forms, Galleries,Files,Users] 
    for model in models:
        model.drop_table()

def create_tables():
    models = [Users, Files,Galleries,Forms,Images] 
    for model in models:
        model.create_table()

def dummy_data():
    drop_tables()
    create_tables()
    load_user_data()
    load_files_data()
    load_galleries_data()
    load_forms_data()
    load_images_data()

def load_user_data():
    Users(uid=1, username="adminUser").save(force_insert=True)

def load_galleries_data():
    Galleries(gid=1, title="Fortran", open_date="2018-01-21 12:00:00", close_date="2018-02-22 12:00:00", banner=2, description="<b>I AM BOLD, I AM FORTRAN, MAKE SURE TO SANITIZE ME </b>" ).save(force_insert=True)

    Galleries(gid=2, title="Golang", open_date="2018-01-21 12:00:00", close_date="2018-02-12 12:00:00", banner=11, description="<em> I am edgy, I am golang, make sure to sanitize me </em>").save(force_insert=True)

def load_files_data():
    Files(fid=1, filetype="pdf", form=1, filename="cv", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/cv.pdf").save(force_insert=True)
    Files(fid=2, filetype="jpeg", form=1, filename="banner", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/banner.jpeg").save(force_insert=True)
    Files(fid=3, filetype="jpg", form=1, filename="image_0", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/image_0.jpg").save(force_insert=True)
    Files(fid=4, filetype="jpg", form=1, filename="image_0_thumb", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/image_0_thumb.jpg").save(force_insert=True)
    Files(fid=5, filetype="jpg", form=1, filename="image_1", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/image_1.jpg").save(force_insert=True)
    Files(fid=6, filetype="jpg", form=1, filename="image_1_thumb", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/image_1_thumb.jpg").save(force_insert=True)
    Files(fid=7, filetype="jpg", form=1, filename="image_2", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/image_2.jpg").save(force_insert=True)
    Files(fid=8, filetype="jpg", form=1, filename="image_2_thumb", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/image_2_thumb.jpg").save(force_insert=True)
    Files(fid=9, filetype="pdf", form=1, filename="statement", filepath="/static/data/Fortran_2018_01_21/John@Backus.me/statement.pdf").save(force_insert=True)

    Files(fid=10, filetype="pdf", form=1, filename="cv", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/cv.pdf").save(force_insert=True)
    Files(fid=11, filetype="png", form=1, filename="banner", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/banner.png").save(force_insert=True)
    Files(fid=12, filetype="jpg", form=1, filename="image_0", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/image_0.jpg").save(force_insert=True)
    Files(fid=13, filetype="jpg", form=1, filename="image_0_thumb", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/image_0_thumb.jpg").save(force_insert=True)
    Files(fid=14, filetype="png", form=1, filename="image_1", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/image_1.png").save(force_insert=True)
    Files(fid=15, filetype="png", form=1, filename="image_1_thumb", filepath="/static/data/Go_2018_01_21_thumb.png").save(force_insert=True)
    Files(fid=16, filetype="png", form=1, filename="image_2", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/image_2.png").save(force_insert=True)
    Files(fid=17, filetype="png", form=1, filename="image_2_thumb", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/image_2_thumb.png").save(force_insert=True)
    Files(fid=18, filetype="pdf", form=1, filename="statement", filepath="/static/data/Go_2018_01_21/Rob@Pike.go/statement.pdf").save(force_insert=True)

def load_forms_data():
    Forms(fid=1, first_name="John", last_name="Backus", street_address="101 Road", city="Fortran", state="KY", email="John@Backus.me",phone_number="1234567890", website="Backus.me", gallery=1, cv=1, personal_statement=9).save(force_insert=True)
    Forms(fid=2, first_name="Rob", last_name="Pike", street_address="101 Pike Road", city="Golang", state="NY", email="Rob@Pike.go",phone_number="0987654321", website="Pike.go", gallery=2, cv=10, personal_statement=18).save(force_insert=True)

def load_images_data():
    Images(iid=1, form=1, fullsize=3, thumbnail=4).save(force_insert=True)
    Images(iid=2, form=1, fullsize=5, thumbnail=6).save(force_insert=True)
    Images(iid=3, form=1, fullsize=7, thumbnail=8).save(force_insert=True)

    Images(iid=4, form=1, fullsize=12, thumbnail=13).save(force_insert=True)
    Images(iid=5, form=1, fullsize=14, thumbnail=15).save(force_insert=True)
    Images(iid=6, form=1, fullsize=16, thumbnail=17).save(force_insert=True)


if __name__ == "__main__":
    dummy_data()


