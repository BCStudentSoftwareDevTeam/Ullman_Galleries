import yaml
import os, sys, glob
from peewee import *


# Allow access to the app/config directory
path = os.getcwd()
test_dir = os.path.join(path,'app/config/')

if os.path.isdir(test_dir):
    sys.path.insert(0,path)
else:
    new_path = os.path.dirname(path)
    sys.path.insert(0,new_path)

class ConfigureApp():
    def __init__(self):
        self.db_choice = None
        self.db_name = None
        self.host = None
        self.username = None
        self.password = None
        self.secret_key = None

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


    def get_db_choice(self):
        self.db_choice = 'mysql'
        return 'mysql'

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
        db_name0 = input('What is the name of your mysql database: ')
        return db_name0

    def get_mysql_variables(self):
        self.host = input('What is your host? ')
        self.username = input('What is your username for msql? ')
        self.password = input('What is your password for mysql? ')
        print ('\nIf you have entered any of these variables incorrectly, they can be changed in secret.yaml.')

    def edit_secret_yaml(self):
        secret_data = {'db':{"db_name":self.db_name, "db_choice":self.db_choice, "host":self.host, "username":self.username, "password":self.password}, "secret_key":self.secret_key,}

        #TODO: Figure out how not to hard code this
        path = os.path.join(sys.path[0],'app/config/secret.yaml')
        with open(path,'w') as outfile:
            yaml.dump(secret_data, outfile, default_flow_style=False)


    def create_mysql_database(self):
        dummy_prompt = self.add_dummy_data_prompt()
        if dummy_prompt:
            self.add_dummy_data()

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
        # Loaded later to prevent initial load of database
        # The model dependency in load_dummy data (import * from app.models) includes utils.py, which auto sets up the connection
        from dummy_data import dummy_data
        dummy_data()


    def main(self):
        self.db_choice    = 'mysql'
        self.db_name      = self.get_db_name()
        self.get_mysql_variables()
        self.secret_key = self.get_secret_key()
        self.edit_secret_yaml()
        self.create_mysql_database()



if __name__ == '__main__':
    create = ConfigureApp()
    create.main()


#TODO:
# Find a way to create the mySQL Database
# Find a way to add dummy data to the mysql database
