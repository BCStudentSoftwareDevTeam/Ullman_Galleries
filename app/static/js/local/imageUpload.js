
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
    acceptedFiles: ".jpg,.jpeg,.pdf,.raw,.png,.docx,.doc,.svg,.gif,.bmp",
    dictDefaultMessage: "Upload Images Here",
    addRemoveLinks: true,
    clickable: true,
    uploadMultiple: true,
    parallelUploads: 100,
    maxFiles: 100,
    error: function(file, error ,xhr){
        file.status = Dropzone.QUEUED;
        file.previewElement.classList.add("dz-error")
        file.previewElement.children[3].firstElementChild.innerText= "Failed to upload file please try again"
        upload_failed = true
    },
   queuecomplete: function(){
   }
})

function submitforms(){
  $("#createApplicationForm").validate({
    errorClass:"text-danger"
  })
  if ($("#createApplicationForm").valid()){
    form = $('#createApplicationForm')[0]
    $.ajax({
        url:'/submit/',
        type:'post',
        data:new FormData(form),
        processData: false,
        contentType: false,
        success:function(){
          $("#fileDropZone").show()
          $("#message").hide()
          $("#next").hide()
          $("#submit").show()
        },
        error: function(){  
          $("#message_text").text("Unable to submit form, please try again")
          $("#message").show()
        }
    });
  }

}
