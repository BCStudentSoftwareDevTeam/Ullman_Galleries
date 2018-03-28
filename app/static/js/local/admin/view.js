if(performance.navigation.type == 2){
   location.reload(true);
}

  CKEDITOR.replace( 'description' );

function reload(){
  setTimeout(function(){
    location.reload();
  }, 2000);
}

function status_change(element,form_id){
  value = $(element).val();
  url = "/view/status/change/" + value + "/" + form_id+"/"

  $.post(url, function(data){
    $("html, body").animate({
      scrollTop: 0
    }, 0);

    location.reload();
  })
}

function submit_text(){
  data = CKEDITOR.instances['description'].getData()
  $.post( "/view/description", {'description': data}, function( data ) {
    location.reload();
  });
}
