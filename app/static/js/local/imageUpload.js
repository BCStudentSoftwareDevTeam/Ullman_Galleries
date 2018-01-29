// Retrieve the GID 
var current_URL = String(document.URL);
var modified_URL = current_URL.split("/")
var space = modified_URL.pop()
var GID= modified_URL.pop()
// DropZone
Dropzone.autoDiscover = false;
var feedbackDropZone = new Dropzone('#fileDropZone',
  {
    paramname: 'file', //The name that will be used to transfer the file
    acceptedFiles: ".jpg,.jpeg,.png",
    url: "/application/submit/"+GID,
    dictDefaultMessage: "Upload files here.",
    addRemoveLinks: true,
    clickable: true
  }
);
