// Retrieve the GID 
var current_URL = String(document.URL);
var modified_URL = current_URL.split("/")
var GID= modified_URL.pop()
// DropZone
Dropzone.autoDiscover = false;
var fileDropZone = new Dropzone('#fileDropZone',
  {
    paramname: 'file', //The name that will be used to transfer the file
    acceptedFiles: ".jpg,.jpeg,.png",
    dictDefaultMessage: "Upload images here.",
    url:"/application/submit/"+GID,
    addRemoveLinks: true,
    clickable: true,
    uploadMultiple: true,
    maxFiles: 100,
    autoProcessQueue: false,
    init: function(){
        var submitButton = document.querySelector('#submit');
        fileDropZone = this;
        submitButton.addEventListener('click',function(){
              fileDropZone.processQueue();
        }
        
    }
  });
      
    