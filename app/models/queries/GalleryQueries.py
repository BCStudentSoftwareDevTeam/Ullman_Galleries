from app.models.Galleries import Galleries
def get(gid):
    """ Retrieves a single gallery object

    Args:
        gid (int): The gid of the gallery model to retrieve 

    Returns:
        Gallery: The gallery object if it exists
        None: If the gallery object does not exist
    """

    if type(gid) is int:
        if Galleries.select().where(Galleries.gid == gid).exists():
            return Galleries.get(Galleries.gid == gid)
    return None
