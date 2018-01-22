def check_empty_list(the_list):
    '''Assures that a list not empty
    Args:
        the_list (list): The list to be checked

    Returns:
        list: If the list is not empty then the original list is returned otherwise None is returned
    '''
    if the_list == []:
        return None
    else:
        return the_list

def check_empty_str(the_string):
    '''Assures that a string is not empty
    Args:
        the_string (str): The string to be checked

    Returns:
        str: If the sting is not empty then the original string is returned otherwise None is returned
    '''
    try:
        if string == '':
            return None
        if string != None:
            result = isinstance(str(string),str)
            if result == False:
                return None
    except Exception as e:
        return None

    return the_string

def list_to_csv_str(the_list):
    '''Converts a list into a comma separated string
    Args:
        the_list (list): The list to be converted 

    Returns:
        str: If the list was not None then a string is returned otherwise None is returned

        The string returned is a comma separated string of the contents of the list
    '''
    check = check_empty_list(the_list)
    if not (check is None):
        csv_str = ",".join(the_list)
        return csv_str
    return None

def csv_str_to_list(the_string):
    '''Converts a comma separated string into a list
    Args:
        the_str (str): The string to be converted 

    Returns:
        list: If the string was not None then a list is returned otherwise None is returned
    '''
    check = check_empty_str(the_string)
    if not (check is None):
        new_list = the_string.split(",")
        return new_list
    return None


