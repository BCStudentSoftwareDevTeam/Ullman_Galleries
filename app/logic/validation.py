# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from app.models import *
from app.models.queries import *
from app.config import * #This import is for testing
from app.logic.absolute_path import *
from functools import wraps
from flask import request, redirect, url_for, flash, abort
import os, re

def getUsernameFromEnv():
  ''' Pulls the user's username from the environment 
  Returns:
    str: The user's username  
  '''
  env = request.environ
  envK = "eppn"
  if envK in env:
    username = env[envK].split("@")[0].split('/')[-1].lower()
    add_user(env, username)
    return username
  else:
    cfg = get_cfg()
    return cfg['user']['tmp']

def doesUserHaveRole(role):
  ''' Pulls the user's username from the environment 
  Args: 
    role (str): Checks to see if a user has a certain role
  Returns:
    boolean: True if user has role, false otherwise
  '''
  #TODO: Delete dummy circumstance before production
  username = getUsernameFromEnv()
  try:
    user = UserQueries.select_single(username)
    if user and role=='admin':
      return True
    else:
      return False
  except Exception as e:
    print(e)
    return False

# def switchRoles(Role):
#   ''' Pulls the user's username from the environment 
#   Args: 
#     role (str): Checks to see if a user has a certain role
#   Returns:
#     boolean: True if user has role, false otherwise
#   '''
#   userName = getUsernameFromEnv()
#   query    = User.update(role=Role).where(User.username==userName)
#   query.execute()
#   return True


# https://realpython.com/blog/python/primer-on-python-decorators/

def require_login ():
  ''' Force user to login before accessing the page
  Returns:
    User: The resulting user object is returned
  '''
  username = getUsernameFromEnv()
  user = UserQueries.select_single(username)
  return user



def require_role (requiredRole):
  ''' Checks to see if a user has a certain role
  Args:
    requiredRole (str): The required roles for access to the page
  Returns:
    function: With a valid role, the function wrapped is returned otherwise a redirect to a 403 is given
  '''
  def decorator (fun):
    @wraps(fun)
    def decorated_fun (*args, **kwargs):
      if type(requiredRole) is tuple:
        for role in requiredRole:
          print(requiredRole)
          if doesUserHaveRole(role):
            print(("User has role: " + role))
            return fun(*args, **kwargs)
        abort(403)
      else:
        if doesUserHaveRole(requiredRole):
          print(('User has role: '+ requiredRole))
          return fun(*args, **kwargs)
        else:
          print(('User does not have role: ' + requiredRole))
          abort(403)
    return decorated_fun
  return decorator

# def add_user(env,username):
#   '''Adds a uer to the environment 
#   Args:
#     env (dict): The environment dictionary
#     username (str): The username to be added to the environment
#
#   Returns:
#     User: The newly added user is returned 
#   '''
#   is_user = UserQueries.select_single(username)
#   print(is_user)
#   if is_user == False:
#     description = request.environ['description'].lower()
#     if description != 'student':
#       try:
#         newUser= UserQueries.insert(username)
#         return newUser
#       except Exception as e:
#         print(e)
#         abort(403)
#     else:
#       abort(404)


