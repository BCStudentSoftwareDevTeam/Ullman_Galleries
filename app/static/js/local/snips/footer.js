$(document).ready(function () {
    archive_color();        
})
// Checks to see if the current page is the archive and if so changes the color of the footer
function archive_color() {
    var page = window.location.href;
    if (page.includes("archive")){
        document.getElementById("contribLink").style.color = "#3498db";
        }
    }
