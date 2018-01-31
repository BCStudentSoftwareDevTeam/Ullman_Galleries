from app.models.Galleries import Galleries
from app.models.Forms import Forms

def get(fid):
    """ Retrieves a single form object

    Args:
        fid (int): The fid of the form model to retrieve 

    Returns:
        Form: The gallery object if it exists
        None: If the form object does not exist
    """

    if type(fid) is int:
        if Forms.select().where(Forms.fid == fid).exists():
            return Forms.get(Forms.fid == fid)
    return None

def get_all_from_gallery(gid):
    """ Retrieves all form object for a single gallery

    Args:
        gid (int): The gid of the gallery model to retrieve forms from

    Returns:
        Forms (list): A list of the form objects for a gallery
        None: If the gallery object does not exist
    """

    if type(gid) is int:
        if Galleries.select().where(Galleries.gid == gid).exists():
            forms = Forms.select().join(Galleries).where(Galleries.gid == gid)
            return list(forms)
    return None
