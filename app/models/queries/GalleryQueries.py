from app.models.Galleries import Galleries
from datetime import datetime

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

def insert(title, open_date, close_date, description, banner, folder_name):
    """ Creates a single gallery object
    
    Args:
        title(str): The title of the gallery
        open_date(datetime): The opening date of gallery submission
        close_date(datetime): The closing date of the gallery submission
        description(str): Description of the gallery
        banner(str): ForeignKeyField for Poster Image
    Returns:
        gid: Primary key of the new Gallery object will be returned
        None: If Gallery object is not saved
    """
    try:
        #TODO: Sanitize description
        gid = Galleries.create(
                        title =title,\
                        open_date = open_date,\
                        close_date = close_date,\
                        description =  description,\
                        banner = banner,\
                        folder_name = folder_name)
        return gid
    except Exception as e:
        print (e)
    return None

def update(gid, title, open_date, close_date, description, banner, folder_name):
    """ Update existing gallery record
    
    Args:
        title(str): The title of the gallery
        open_date(datetime): The opening date of gallery submission
        close_date(datetime): The closing date of the gallery submission
        description(str): Description of the gallery
        banner(str): ForeignKeyField for Poster Image
    Returns:
        gid: Primary key of the updated Gallery object will be returned
        None: If Gallery object is not saved
    """
    try:
        if Galleries.select().where(Galleries.gid == gid).exists():
            gallery              = Galleries.get(Galleries.gid == gid)
            gallery.title        = title
            gallery.open_date    = open_date
            gallery.close_date   = close_date
            gallery.description  = description
            gallery.banner       = banner
            gallery.folder_name  = folder_name
            gallery.save()
        return gid
    except Exception as e:
        print (e)
    return None

def get_status(gid, date_format="%m/%d/%Y"):
    
    """ Determine gallery status
    
    Args:
        gid: The gallery id for each gallery
    Optional:
        date_format (str): The strftime formatting for the DateTimeFields (default: %m/%d/%y)
    Returns:
        String with gallery status and relevant dates
    """
    try:
        if Galleries.select().where(Galleries.gid == gid).exists():
            gallery = Galleries.get(Galleries.gid == gid)
            title=gallery.title
            open_date=gallery.open_date
            close_date= gallery.close_date
            status = None
            today = datetime.now()
            if today >= open_date and today >= close_date: 
                status ="Closed" + " " + close_date.strftime(date_format)
            if today <= open_date and today <= close_date: 
                status = "Coming Soon " +" " + open_date.strftime(date_format)
            if today >= open_date and today <= close_date: 
                status = "Active " + " " + open_date.strftime(date_format) + " " + "to" + " " + close_date.strftime(date_format)
        return status
    except Exception as e:
        print (e)
    return None
