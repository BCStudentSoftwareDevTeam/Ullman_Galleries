# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from app.models import *
from app.models.queries import *
# from app.config import * #This import is for testing
from app.logic.absolute_path import *
from functools import wraps
from flask import request, redirect, url_for, flash, abort
from flask import session 
from flask_security.core import current_user
import os, re

def doesUserHaveRole(role):
  ''' Pulls the user's username from the session
  Args: 
    role (str): Checks to see if a user has a certain role
  Returns:
    boolean: True if user has role, false otherwise
  '''
  if role == "anonymous":
      return current_user.is_anonymous
  if current_user.has_role(role):
      return True
  return False








