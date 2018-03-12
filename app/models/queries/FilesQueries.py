from app.models.Files import Files
def get(fid):
    """ Retrieves a single gallery object

    Args:
        fid (int): The fid of the file model to retrieve 

    Returns:
        File: The file object if it exists
        None: If the file object does not exist
    """

    if type(fid) is int:
        if Files.select().where(Files.fid == fid).exists():
            return Files.get(Files.fid == fid)
    return None

def update(fid, filepath=None, filename=None, filetype=None):
    """ Update existing file record
    
    Args:
        
    Returns:
        fid: Primary key of the updated Gallery object will be returned None: If Gallery object is not saved
    """
    try:
        if Files.select().where(Files.fid == fid).exists():
            file = Files.get(Files.fid == fid)
            
            if filetype != None:
                file.filetype = filetype
            
            if filename != None:
                file.filename = filename
            
            if filepath != None:
                file.filepath = filepath
        return fid
    except Exception as e:
        print (e)
    return None

def insert(filepath, filename, filetype):
    """ Insert a new file record
    Args:
        filepath (str): The filepath of the new file to be added
        filename (str): The filename of the new file, minus the extension
        filetype (str): The extension of the new file
    
    Returns:
        fid (File): The newly created File
        None: If unable to create File 
    
    """
    try:
        fid = Files.create(filepath = filepath,\
                        filename = filename,\
                        filetype = filetype)
        return fid
    except Exception as e:
        print (e)
    return None

def file_count(fid):
    """ Get the number of files submitted by a user
    Args:
        fid (Form): The form of the user, whose images need to be counted
    
    Returns: 
        count (int): The number of images submitted by the user.
    """
    if Files.select().where(Files.fid== fid).exists():
        return Files.select().where(Files.fid == fid).count()
    else:
        return 0

def get_all_from_fid(fid):
    """
        Returns a list of all the files attached to a form
    Args:
        fid (Form): The form of the user, whose files need to be counted
    Returns: 
        files (list): A list of all the files attached to a user 
    """
    if Files.select().where(Files.fid == fid).exists():
        return list(Files.select().where(Files.fid == fid))
    else:
        return list()
