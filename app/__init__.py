from flask import Flask, render_template
from app.config import loadConfig

import sys

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
    
    @app.errorhandler(403)
    def access_denied(e):
        return render_template('views/403.html', cfg=cfg), 403
    
    @app.errorhandler(404)
    def pageNotFound(e):
        return render_template('views/404.html', cfg=cfg), 404
    return app
