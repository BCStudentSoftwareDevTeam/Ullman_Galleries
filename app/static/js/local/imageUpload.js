
$(window).on('load',function(){
    $('#uploadModal').modal('show');
})

function closeModal(){
    $('#uploadModal').modal('hide');
}
Dropzone.autoDiscover = false;
var fileDropZone = new Dropzone('#fileDropZone',{
    paramname: 'file', //The name that will be used to transfer the file
    acceptedFiles: ".jpg,.jpeg,.png",
    dictDefaultMessage: "Upload images here.",
    addRemoveLinks: true,
    clickable: true,
    uploadMultiple: true,
    parallelUploads: 50,
    maxFiles: 50,
    autoProcessQueue: false,
    init: function(){
        var submitButton = document.querySelector('#submit');
        fileDropZone = this;
        submitButton.addEventListener('click',function(){
              fileDropZone.processQueue();
        });
        
        this.on("successmultiple", function(files, response) {
        console.log(response);
        window.location.replace("/application/review/"+response);
        });
        
        this.on("errormultiple", function(files, response) {
        // Gets triggered when there was an error sending the files.
        // Maybe show form again, and notify user of error
        console.log(response);
        });
    }
  });
      
    
