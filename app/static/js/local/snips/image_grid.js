function delete_image(element){
  $.post( "/delete/image", { filepath: element.dataset['filepath']} , function(data){
    id = "#"+element.dataset['div']
    $(id).fadeOut("slow")
  })
    .fail(function(data){
      $("#message").fadeOut("slow")
      $("#message").fadeIn("fast")
      $("#message_text").text(data.responseText)
      $("#message").attr("class", "alert alert-danger alert-dismissable")
      $("html, body").animate({
            scrollTop: 0
          }, 500);  
    })

}

function enlarge_image(element){

   $('#imagepreview').attr('src', $(element).data()['img']); // here asign the image to the modal when the user click the enlarge link
   $('#modal_download').attr('href', $(element).data()['img']); // here asign the image to the modal when the user click the enlarge link
   $('#expand_image_modal').modal('show'); // imagemodal is the id attribute assigned to the bootstrap modal, then i use the show function
}

