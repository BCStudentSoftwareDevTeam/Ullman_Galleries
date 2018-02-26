
$(window).on('load',function(){
    $('#uploadModal').modal('show');
}) 
function closeModal(){
    $('#uploadModal').modal('hide');
}
upload_failed = false
Dropzone.autoDiscover = false;

$("#fileDropZone").dropzone({
    paramname: 'file', //The name that will be used to transfer the file
    acceptedFiles: ".jpg,.jpeg,.png",
    dictDefaultMessage: "Upload images here.",
    addRemoveLinks: true,
    clickable: true,
    uploadMultiple: true,
    parallelUploads: 100,
    maxFiles: 100,
    autoProcessQueue: false,
    error: function(file, error ,xhr){
        file.status = Dropzone.QUEUED;
        upload_failed = true
    },
   queuecomplete: function(){
      if (upload_failed){
        $("#message_text").text("Failed to upload files, please try again")
        $("#message").show()
      }
   }
})

function submitforms(){
    $.ajax({
        url:'/submit/',
        type:'post',
        data:$('#createApplicationForm').serialize(),
        success:function(){
         console.log($("#fileDropZone")[0].dropzone.processQueue())
        }
    });
    // window.location = "/review/";

}
