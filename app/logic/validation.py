# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from app.models import *
from app.models.queries import *
from app.config import * #This import is for testing
from app.logic.absolute_path import *
from functools import wraps
from flask import request, redirect, url_for, flash, abort
from flask import session 
import os, re

def doesUserHaveRole(role):
  ''' Pulls the user's username from the session
  Args: 
    role (str): Checks to see if a user has a certain role
  Returns:
    boolean: True if user has role, false otherwise
  '''
  if "user_id" in session:
      user_id = session["user_id"]
      if user_id is not None:
        if Users.select(Users.id == user_id).exists():
          return Users.get(Users.id == user_id).has_role(role)
  return False








