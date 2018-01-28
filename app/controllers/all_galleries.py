from app.allImports import * 
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session
from app.models.Forms import *
from app.models.Galleries import *
from datetime import datetime



@app.route('/', methods=["GET","POST"])
def all_galleries():
  
    formGalleryIds=[] 
    gallaryIds = []
    
    
    map1={} #maps gallery ids and titles
    map2={} #maps gallary to the total numbe of submissions it has
    map3 = {} #maps gallery to its status e.g closed,open,active
    map4 = {} #Stores final dates for each gallery depending on its status.
    
    
    
    
    
    for gallery in Galleries.select():
        map1[gallery.gid]=gallery.title
        gallaryIds.append(gallery.gid)
        
    for form in Forms.select():
        formGalleryIds.append(form.gallery_id)
        
    
    #initializing gallery submission count
    for gallerycount in gallaryIds:
        map2[gallerycount] = 0
        
    
    #Counting number of submissions in each gallery
    for galleryid in formGalleryIds:
        if galleryid in map2:
            map2[galleryid] +=1
            
    
    today = datetime.now() #For purposes of determining the status of a galler
    for gallery_name in map2:
        #getting dates for each gallery
        obj=Galleries.get(gid=gallery_name)
        opened= obj.open_date
        closed=obj.close_date
        
        
        if today >= opened and today >= closed:
            #if closed deadline passed,status=closed
            map3[gallery_name]="Closed :"
            close_date=str(closed)
            map4[gallery_name]=close_date
        if today <= opened and today <= closed:
            #if both open and closed deadlines have not passed, we lable it as "coming soon"
            map3[gallery_name]="Coming Soon :"
            open_date=str(opened)
            map4[gallery_name]=open_date
            
        if today >= opened and today <= closed:
            #if gallery opened but has not closed, we label it as active
            map3[gallery_name]="Active :"
            active_date=str(opened)
            active_closed_date=str(closed)
            active_period = active_date + " - "  + active_closed_date
            map4[gallery_name]=active_period
            
   
    return render_template('views/all_galleries.html',
                                                map1=map1,
                                                map2=map2,
                                                map3=map3,
                                                map4=map4)


