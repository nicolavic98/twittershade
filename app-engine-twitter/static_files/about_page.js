function Expand(){
  $('.expandable').on('click', function() {
    $(this).toggleClass('show-description');
  });
}
$(document).ready(Expand);
