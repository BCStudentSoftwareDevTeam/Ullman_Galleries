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
        console.log("It is working!");
        fileDropZone = this;
        submitButton.addEventListener('click',function(){
            console.log("button clicked");
            
            if (fileDropZone.files.length > 0){
              fileDropZone.processQueue();
            } else {
              // ajax form post
            }
            console.log("still working!");
        });
      
      // $('#createApplicationForm').ajaxForm();
      
      // Listen to the sendingmultiple event. In this case, it's the sendingmultiple event instead
      // of the sending event because uploadMultiple is set to true.
      this.on("sendingmultiple", function(file, xhr, formData) {
        // Gets triggered when the form is actually being sent.
        // Hide the success button or the complete form.
        
        // var formValues = $('#createApplicationForm').serializeObject()
        // $.each(formValues, function(key, value){
        //     //formData.append(key,value);
        //     console.log(key, value);
        // });
        
      });
      this.on("successmultiple", function(files, response) {
        console.log(response);
        //window.location.replace("http://www.google.com");
      });
      this.on("errormultiple", function(files, response) {
        // Gets triggered when there was an error sending the files.
        // Maybe show form again, and notify user of error
        console.log(response);
      });

    }
  });
