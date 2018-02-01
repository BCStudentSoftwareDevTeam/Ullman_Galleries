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