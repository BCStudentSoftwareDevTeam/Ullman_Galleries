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
        fid: Primary key of the updated Gallery object will be returned
        None: If Gallery object is not saved
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