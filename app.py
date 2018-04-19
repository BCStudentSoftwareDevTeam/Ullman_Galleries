'''
app.py is the starting point of the application; to run the app, in the console, you run "python app.py"

This file should not change often, except maybe to rename the application from "app" to something more meaningful
such as "helloWorldForm"

To rename the app, you need to make three changes:
1) Change  "from app import app" to "from helloWorldForm import app"
2) Rename the "app" folder to "helloWorldForm"
3) Rename this file to "helloWorldForm.py"

'''
import os
import sys
from app.config.loadConfig import get_secret_cfg



# Use local path if local variable is provided
if os.getenv("LOCAL"):
    if os.getenv("LOCAL").lower() == 'true':
        sys.path.insert(0,os.getcwd())
    else:
        sys.path.insert(0,os.getenv("LOCAL"))
else:
    sys.path.insert(0,'/home/ubuntu/workspace/')


secret_cfg = get_secret_cfg()
os.environ["MYSQL_HOST"] = secret_cfg['db']['host']
os.environ["MYSQL_DB"] = secret_cfg['db']['db_name']
os.environ["MYSQL_PASSWORD"] = secret_cfg['db']['password']
os.environ["MYSQL_USERNAME"] = secret_cfg['db']['username']
os.environ["APP_SECRET_KEY"] = secret_cfg['secret_key']
os.environ["SECURITY_PASSWORD_SALT"] = secret_cfg['salt']


# Builds the server configuration
if os.getenv('IP'):
  IP    = os.getenv('IP')
else:
  IP    = '0.0.0.0'

if os.getenv('PORT'):
  PORT  = int(os.getenv('PORT'))
else:
  PORT  = 8080

# Print statements go to your log file in production; to your console while developing
from app import create_app
print(("Running server at http://{0}:{1}/".format(IP, PORT)))
app = create_app('development')
app.run(host = IP, port = PORT, debug = True, threaded = True)
