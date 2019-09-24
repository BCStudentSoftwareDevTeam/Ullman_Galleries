'''
This script loads the yaml file, which holds all 
configuration information.
'''

from app.logic.absolute_path import *
import yaml, os
import logging

def load_config(file):
    if os.path.exists(getAbsolutePath(file)):
        with open(file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return cfg
    else:
        return None

def get_cfg():
    config_abs_path = getAbsolutePath('app/config','config.yaml')
    cfg             = load_config(config_abs_path)
    return cfg
    
def get_secret_cfg():
    secret_abs_path = getAbsolutePath('app/config','secret.yaml')
    secret_cfg      = load_config(secret_abs_path)
    return secret_cfg
