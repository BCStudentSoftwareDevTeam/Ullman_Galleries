import yaml
import os, sys, glob
from peewee import *
import inspect
import hashlib
# http://flask.pocoo.org/snippets/54/
from werkzeug.security import generate_password_hash
from dummy_data import load_dummy

path = os.getcwd()
test_dir = os.path.join(path,'app/config/')
if os.path.isdir(test_dir):
    sys.path.insert(0,path)
else:
    new_path = os.path.dirname(path)
    sys.path.insert(0,new_path)

from app.models.util import getDB

class ConfigureApp():
    def __init__(self):
        self.db_choice = None
        self.db_name = None
        self.host = None
        self.username = None
        self.password = None
        self.secret_key = None
        self.conf = self.load_config('config.yaml')

    def get_abs_path(self,relaitivePath):
        filepath = os.path.join(sys.path[0],relaitivePath)
        return filepath

    def get_model_filenames(self):
            filenames = []
            model_dir = 'app/models'
            for file in glob.glob(model_dir + "/*.py"):
                ignore_list = ['__init__.py','util.py']
                if (os.path.basename(file) not in ignore_list):
                    print("File: {0}".format(file))
                    filenames.append(os.path.splitext(os.path.basename(file))[0])
            print(filenames)
            return filenames

    def import_peewee_tables(self):
        model_filenames = self.get_model_filenames()
        models_list = []
        for model in model_filenames:
            package = "app.models"
            peewee_table = getattr(__import__(package,fromlist=[model]), model)
            models_list.append(peewee_table)
        print(models_list)
        return models_list

    def load_config(self,filename):
        rel_path = 'app/config/' + filename
        file_abs_path = self.get_abs_path(rel_path)
        with open(file_abs_path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg

    def get_db_choice(self):
        self.db_choice = 'mysql'
        return 'mysql'
        # print('[1]: SQLite\n[2]: MySQL')
        # while True:
        #     user_input = input('What kind of database are you using? ')
        #     if (user_input.lower() == 'sqlite') or (user_input == '1'):
        #         self.db_choice = 'sqlite'
        #         return 'sqlite'
        #     elif (user_input.lower() == 'mysql') or (user_input == '2'):
        #         self.db_choice = 'mysql'
        #         return 'mysql'
            # else:
            #     print('\nERROR: Invaild Response\tPlease type either the name of the software of its corresponding number. eg(Sqlite or 1)')

    def get_secret_key(self):
        print('\nFlask Session Cookies are cryptographically signed, which basically')
        print('means that in order for a user to modify a session cookie they would')
        print('need a secret key, which is a functionality required by this application.\n')
        while True:
            secret_key0 = input('Therefore, what would you like the secret key to be for your application? ')
            secret_key1 = input('Please type the secret key again: ')
            if secret_key0 == secret_key1:
                print("Thank you the secret key has been saved inside of secret.yaml, and can be changed at anypoint through modifing that file.")
                return secret_key0
            else:
                print('The two secret keys did not match.')

    def get_db_name(self):
        # print('Please exclude any path or extention details, eg( "data/" or ".sqlite").')
        db_name0 = 'localhost'
        db_name0 = input('What is the name of your mysql database: ')
        return db_name0

    def get_mysql_variables(self):
        self.host = input('What is your host? ')
        self.username = input('What is your username for msql? ')
        self.password = input('What is your password for mysql? ')
        print ('\nIf you have entered any of these variables incorrectly, they can be changed in secret.yaml.')

    def edit_secret_yaml(self):
        #values_list should be ordered:
        #  [db_name,host,username,password,secret_key]
        if self.db_choice == 'sqlite':
            secret_data = {"db":{"db_name":self.db_name, "db_choice":self.db_choice}, "secret_key":self.secret_key}
        else:
            secret_data = {'db':{"db_name":self.db_name, "db_choice":self.db_choice, "host":self.host, "username":self.username, "password":self.password}, "secret_key":self.secret_key,}
        #TODO: Figure out how not to hard code this
        path = os.path.join(sys.path[0],'app/config/secret.yaml')
        with open(path,'w') as outfile:
            yaml.dump(secret_data, outfile, default_flow_style=False)

    def create_sqlite_database(self):
        db_abs_path = self.get_abs_path(self.db_name)
        print(db_abs_path)

        check = self.no_db_file()
        if check:
            self.create_file()
            self.create_tables('sqlite')
        else:
            print('Creation of the SQLite database has stopped.')
        dummy_prompt = self.add_dummy_data_prompt()
        if dummy_prompt:
            self.add_dummy_data()

    def create_mysql_database(self):
        dummy_prompt = self.add_dummy_data_prompt()
        self.create_tables('mysql')
        if dummy_prompt:
            self.add_dummy_data()

    def remove_db(self):
        try:
            os.remove(self.db_name)
            db_abs_path = self.get_abs_path(self.db_name)
            print(("\t...Removing {0}.".format(db_abs_path)))
        except OSError:
            print(OSError)
            pass

    def no_db_file(self):
        if os.path.isfile(self.db_name):
            print(("WARNING: Database ({0}) already exists in the system.".format(self.db_name)))
            cont = None
            while True:
                print ('Continuing this setup will DELETE your current sqlite file')
                user_input = input('Would you like to continue? (y/n): ')
                if (user_input.lower() == 'yes') or (user_input.lower() == 'y'):
                    self.remove_db()
                    return True
                elif (user_input.lower() == 'no') or (user_input.lower() == 'n'):
                    return False
                else:
                    print('\nERROR: Invaild Response\tPlease respond with either yes/y or no/n.')
        return True

    def add_dummy_data_prompt(self):
        while True:
            user_input = input('Would you like to add some default testing data to your db? (Y/N) ')
            if (user_input.lower() == 'y') or (user_input.lower() == 'yes'):
                return True
            elif (user_input.lower() == 'n') or (user_input.lower()=='no'):
                return False
            else:
                print('\n ERROR: Invaild Response\tPlease respond with either yes/y or no/n.')

    def add_dummy_data(self):
        load_dummy()


    def create_file(self):
        db_abs_path = self.get_abs_path(self.db_name)
        print('Creating empty SQLite file: {0}'.format(db_abs_path))
        open(db_abs_path, 'a').close()
        return True

    def create_tables(self,database_type):
        database = None
        if database_type == "sqlite":
            db_abs_path = self.get_abs_path(self.db_name)
            database = SqliteDatabase(db_abs_path)
        else:
            database = getDB()
            database.connect()

        models = self.import_peewee_tables()
        for model in models:
            database.create_table(model,safe=True)



    def main(self):
        self.db_choice    = self.get_db_choice()
        self.db_name      = self.get_db_name()
        if self.db_choice == 'sqlite':
            self.db_name = 'data/' + self.db_name + '.sqlite'
        else:
            self.get_mysql_variables()
        self.secret_key = self.get_secret_key()
        self.edit_secret_yaml()
        if self.db_choice == 'sqlite':
            self.create_sqlite_database()
        if self.db_choice == 'mysql':
            self.create_mysql_database()



if __name__ == '__main__':
    create = ConfigureApp()
    create.main()

#TODO:
# Find a way to create the mySQL Database
# Find a way to add dummy data to the mysql database
