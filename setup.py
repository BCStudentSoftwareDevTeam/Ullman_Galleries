# coding=utf-8

from setuptools import setup, find_packages
import os
import sys

if sys.version_info[0] != 3:
    print("This script requires Python 3")
    exit()


path = os.path.dirname(os.path.realpath(__file__))
print(path)
sys.path.insert(0, path)

#When setuptools run it pulls these tools from Pypi
os.system('git update-index --assume-unchanged app/config/secret.yaml')
def require_venv():
    try:
        venv_dir = (os.path.isdir('venv'))
        if venv_dir == False:
            print('Creating venv directory...\n')
            os.system('virtualenv --python python3 venv')
        venv_active = hasattr(sys,'real_prefix')
        if venv_active == False:
            print('Activating venv...\n')
            activate_file = "venv/bin/activate_this.py"
            exec(compile(open(activate_file).read(), activate_file, 'exec'), dict(__file__=activate_file))
    except Exception as e:
        print('This setup requires virtualenv.')

INSTALL_REQUIRES = [
    "Flask>=0.11.1",
    "Jinja2>=2.8,<2.9",
    "peewee>=2.8.1",
    "Flask-Admin>=1.4.0",
    "wtf-peewee>=0.2.6",
    "XlsxWriter",
    "PyYAML",
    "email_validator",
    "Flask-Script",
    "flask-mysqldb",
    "flask-login",
    "PIL"
    ]
    
def parameters():
    name="Ullman Galleries"
    description="A gallery entry application management software"
    long_description = open("README.md").read()
    install_requires = INSTALL_REQUIRES
    packages = find_packages(where="app")
    package_dir = {
        "": "app",
    }
    include_package_data=True
    return locals()

require_venv() 
setup(**parameters())
