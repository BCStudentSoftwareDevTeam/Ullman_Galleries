# '''
# This file sets up the virtual environment. 
# Run "source setup.sh" each time you want to run the app. 
# ''' 
FLASK_VERSION="${FLASK_VERSION:-0.12.2}"              #0.12.2
PEEWEE_VERSION="${PEEWEE_VERSION:-3.2.0}"             #3.2.0
PYAML_VERSION="${PYAML_VERSION:-3.12}"                #3.12
XLSXWRITER_VERSION="${XLSXWRITER_VERSION:-1.0.2}"     #1.0.2
WTF_PEEWEE_VERSION="${WTF_PEEWEE_VERSION:-3.0.0}"     #3.0.0
FLASK_LOGIN_VERSION="${FLASK_LOGIN_VERSION:-0.4.1}"   #0.4.1
FLASK_MYSQLDB="${FLASK_MYSQLDB:-0.2.0}"               # 0.2.0
FLASK_SECURITY_VERSION="${FLASK_SECURITY_VERSION:-3.0.0}"   #3.0.0
BLEACH_VERSION="${BLEACH_VERSION:-2.1.3}"             #2.1.3
BCRYPT_VERSION="${BCRYPT_VERSION:-2.1.3}"             #2.1.3






if [ ! -d venv ]
then
  git update-index --assume-unchanged app/config/secret.yaml
  virtualenv --python python3 venv
  . venv/bin/activate
  pip install "flask==$FLASK_VERSION"
  pip install "peewee==$PEEWEE_VERSION"
  pip install "pyyaml==$PYAML_VERSION"
  pip install "XlsxWriter==$XLSXWRITER_VERSION"
  pip install "wtf-peewee==$WTF_PEEWEE_VERSION"
  pip install "flask_security==$FLASK_SECURITY_VERSION"
  pip install "bcrypt==$BCRYPT_VERSION"
  pip intalll "flask-mysqldb==$FLASK_MYSQLDB"
  pip install "bleach==$BLEACH_VERSION"
else
  . venv/bin/activate
fi


if [ ! -f app/config/secret.yaml ]
then
  if [ "${C9_USER}" ]
  then
    mysql -u root --execute="CREATE DATABASE Ulmann"
    echo "PLEASE USE THE FOLLOWING SETTINGS FOR YOUR SECRET SETUP"
    echo "mysql database: Ulmann"
    echo "Hostname: localhost"
    echo "username: ${C9_USER}"
    echo "password: (LEAVE EMPTY)"
  fi
  python scripts/ConfigureApp.py
fi
