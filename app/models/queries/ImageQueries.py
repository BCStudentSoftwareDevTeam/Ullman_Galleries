from app.models.Images import Images
from app.models.Files import Files

def insert(form, fullsize, thumbnail):
    """ Insert a new file record
    Args:
        filepath (str): The filepath of the new file to be added
        filename (str): The filename of the new file, minus the extension
        filetype (str): The extension of the new file
    Returns: fid (File): The newly created File
        None: If unable to create File 
    
    """
    try:
        iid = Images(form=form,
                            fullsize=fullsize,
                            thumbnail=thumbnail)
        iid.save()
        return iid
    except Exception as e:
        print (e)
    return None
    
        
def file_count(fid):
    """ Get the number of images submitted by a user
    Args:
        fid (Form): The form of the user, whose images need to be counted
    
    Returns: 
        count (int): The number of images submitted by the user.
    """
    if Images.select().where(Images.form == fid).exists():
        return Images.select().where(Images.form== fid).count()
    else:
        return 0

def get_form_images(fid):
    """ Get all images associated with a single form
    Args:
        fid (Form): The form of the user, whose images are needed
    Returns: 
        images (list (Image)): A list of all the images uploaded by a user 
    """
    if Images.select().where(Images.form == fid).exists():
        return list(Images.select().where(Images.form == fid))
    return None


