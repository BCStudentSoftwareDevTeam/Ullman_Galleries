function status_change(element){
  value = $(element).val()
  url = "/status/change/" + value + "/"
  $.post(url, function(data){
    $("html, body").animate({
      scrollTop: 0
    }, 0);
    location.reload();
  })
}

