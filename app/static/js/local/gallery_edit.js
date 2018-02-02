CKEDITOR.replace( 'description', {
    customConfig: '/static/js/ckeditor/custom_config.js'
});

$(function() {
    $('#open_date').datetimepicker({
        format: 'MM/DD/YYYY'
    });
    if($('#open_date').attr("value")!=""){
        value = moment($('#open_date').attr("value"), "YYYY-MM-DD HH:mm:ss");
        $('#open_date').data("DateTimePicker").defaultDate(value);
    }
    
});

$(function() {
    $('#close_date').datetimepicker({
        format: 'MM/DD/YYYY'
    });
    
    if($('#close_date').attr("value")!=""){
        value = moment($('#close_date').attr("value"), "YYYY-MM-DD HH:mm:ss");
        $('#close_date').data("DateTimePicker").defaultDate(value);
    }
    
});

Dropzone.options.galleryEditDropzone = { // The camelized version of the ID of the form element

  // The configuration we've talked about above
  autoProcessQueue: false,
  uploadMultiple: true,
  parallelUploads: 100,
  maxFiles: 100,

  // The setting up of the dropzone
  init: function() {
    var myDropzone = this;

    // First change the button to actually tell Dropzone to process the queue.
    this.element.querySelector("button[type=submit]").addEventListener("click", function(e) {
      // Make sure that the form isn't actually being sent.
      e.preventDefault();
      e.stopPropagation();
      myDropzone.processQueue();
    });

    // Listen to the sendingmultiple event. In this case, it's the sendingmultiple event instead
    // of the sending event because uploadMultiple is set to true.
    this.on("sendingmultiple", function() {
      // Gets triggered when the form is actually being sent.
      // Hide the success button or the complete form.
    });
    this.on("successmultiple", function(files, response) {
      // Gets triggered when the files have successfully been sent.
      // Redirect user or notify of success.
    });
    this.on("errormultiple", function(files, response) {
      // Gets triggered when there was an error sending the files.
      // Maybe show form again, and notify user of error
    });
  }
 
}