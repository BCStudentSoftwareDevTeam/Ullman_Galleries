function remove(){
  if (filepath){
    $.post( remove_url, { filepath: filepath }, function(data){
        $("#pre_exist").hide()
        $("#new").show()
        $("#next").prop("disabled", "true")
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
    }else{
    $("#pre_exist").hide()
    $("#new").show()
    $("#next").prop("disabled", "true")
  }
}

