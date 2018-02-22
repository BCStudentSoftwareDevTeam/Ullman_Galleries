
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
    parallelUploads: 100,
    maxFiles: 100,
    autoProcessQueue: true,
    init: function(){
        var submitButton = document.querySelector('#submit');
        fileDropZone = this;
        submitButton.addEventListener('click',function(){
              fileDropZone.processQueue();
        });

        this.on("successmultiple", function(files, response) {
          window.location.replace("/review/");
        });

        this.on("errormultiple", function(files, response) {
        });
    }
  });
