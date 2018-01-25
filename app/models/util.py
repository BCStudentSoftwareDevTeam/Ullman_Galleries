from app.config.loadConfig import *
from app.logic.absolute_path import *
from peewee import *
import os

def getDB ():
  config_abs_path = getAbsolutePath('app/config','config.yaml')
  cfg                   = load_config(config_abs_path)
  secret_config_path    = getAbsolutePath('app/config','secret.yaml')
  secret                = load_config(secret_config_path)
  db_name               = secret['db']['db_name']
  db_choice             = secret['db']['db_choice']
  theDB                 = None

  if db_choice  == "sqlite":
      db_abs_path       = getAbsolutePath(cfg['databases']["mainDB"])
      theDB             = SqliteDatabase (db_abs_path, pragmas = ( ('busy_timeout',  100), ('journal_mode', 'WAL')), threadlocals = True)
  else:
      host              = secret['db']['host']
      username          = secret['db']['username']
      password          = secret['db']['password']
      theDB             = MySQLDatabase ( db_name, host = host, user = username, passwd = password)
  return theDB

mainDB = getDB()
class baseModel(Model):
  class Meta:
    database = mainDB

