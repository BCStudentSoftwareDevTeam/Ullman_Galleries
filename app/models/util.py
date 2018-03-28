from app.config.loadConfig import *
from app.logic.absolute_path import *
from peewee import *
import os
def getDB():
  db_name               = os.environ["MYSQL_DB"]
  theDB                 = None
  host              = os.environ['MYSQL_HOST']
  username          = os.environ["MYSQL_USERNAME"]
  password          = os.environ["MYSQL_PASSWORD"]
  theDB             = MySQLDatabase ( db_name, host = host, user = username, passwd = password)
  return theDB

mainDB = getDB()
class baseModel(Model):
  class Meta:
    database = mainDB

