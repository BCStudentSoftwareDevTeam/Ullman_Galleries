from app.models import Users
def select_all(self):
    '''Selects all users
    Args:
        None
    Return:
        SelectQuery: all users in the database
        None: If unable to connect None is returned
    '''
    try:
      users = Users.select().order_by(Users.username)
      return users
    except Exception as e:
      return None

def insert(username):
    '''An insert query to add a new user
    Args:
      username  (str):  The user's username
    Return:
      User: The newly created user
      False: if unsuccessful
    '''
    if checkStrings(username):
        try:
            user = Users(username=username)
            user.save(force_insert=True)
            return user
        except Exception as e:
            # Log Exception
            print(e)
    return False

def select_single(username):
    '''Selects a single user from the database
    Args:
      username  (str):  The user's username
    Return:
      User: The selected user
      False: if unsuccessful
    '''
    if checkStrings(username):
      try:
        user=Users.get(Users.username==username)
        return user
      except Exception as e:
        print(e)
    return False

def checkStrings(string):
    if type(string) is str and len(string) > 1:
        return True
    else:
        return False
