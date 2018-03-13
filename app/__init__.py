from flask import Flask, render_template
from app.config import loadConfig
from flask_security import Security, PeeweeUserDatastore, utils
import sys
from app.models.Role import Role
from app.models.Users import Users
from app.models.UserRoles import UserRoles
from app.models.util import getDB

sys.dont_write_bytecode = True

''' We are following the application factory
    More information at http://flask.pocoo.org/docs/0.12/patterns/appfactories/
'''

def create_app(config_filename):
    from app.controllers.admin import admin
    from app.controllers.public import public


    app = Flask(__name__)

    secret_cfg = loadConfig.get_secret_cfg()
    cfg = loadConfig.get_cfg()
    app.secret_key = secret_cfg['secret_key']

    app.register_blueprint(admin)
    app.register_blueprint(public)
    mainDB = getDB()
    user_datastore = PeeweeUserDatastore(mainDB, Users, Role, UserRoles)


    # app.config["SECURITY_SEND_REGISTER_EMAIL"] = False
    app.config["SECURITY_PASSWORD_SALT"] = "MUST BE SET"

    security = Security(app, user_datastore)

    # @app.before_first_request
    # def create_user():
    #     user = user_datastore.create_user(email='me@mydomain.com',password=utils.encrypt_password('password'),role='admin')
    #     role =  user_datastore.create_role(name='admin')
    #     user_datastore.add_role_to_user(user, role)


    @app.errorhandler(403)
    def access_denied(e):
        return render_template('views/403.html', cfg=cfg), 403

    @app.errorhandler(404)
    def pageNotFound(e):
        return render_template('views/404.html', cfg=cfg), 404
    return app
