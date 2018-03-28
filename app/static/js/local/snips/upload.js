
$(window).on('load',function(){
    $('#uploadModal').modal('show');
}) 
function closeModal(){
    $('#uploadModal').modal('hide');
}
Dropzone.autoDiscover = false;

$("#Dropzone").dropzone({
    paramname: 'file', //The name that will be used to transfer the file
    acceptedFiles: acceptedFiles,
    dictDefaultMessage: message,
    addRemoveLinks: true,
    uploadMultiple: true,
    maxFiles: maxFiles,
    init: function(){
      this.on("success", function(){
        $('#next').prop("disabled",false)
      });
      this.on("removedfile", function (file){
        if (this.files.length == 0){
          $('#next').prop("disabled",true)
        }
      });

    }
})

