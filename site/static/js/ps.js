(function( ps, $, undefined) {
  var baseUrl = "static/bios"
    , $activePopup
  ;

  ps.showBio = function(netid) {
    $('#mask').removeClass('hidden');
    $activePopup = $('#' + netid);
    $activePopup.removeClass('hidden');
    $('#mask').click(ps.closeBio);
    $('.newsfeed').css('overflow','hidden');
  };
  ps.closeBio = function() {
    $activePopup.addClass('hidden');
    $('#mask').addClass('hidden');
    $('.newsfeed').css('overflow','auto');
  };
  
}(window.ps = window.ps || {}, jQuery))
