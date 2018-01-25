// DropZone
Dropzone.autoDiscover = false;
var feedbackDropZone = new Dropzone('#fileDropZone',
  {
    paramname: 'file', //The name that will be used to transfer the file
    acceptedFiles: ".jpg,.jpeg",
    // url: "/application/submit,
    dictDefaultMessage: "Upload images here.",
    addRemoveLinks: true,
    clickable: true
  }
);
