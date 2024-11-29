$(function () { // function executes once DOM is loaded
  const amen = {};
  $('div.amenities input[type="checkbox"]').change(function () { // listen for changes on checkbox
    if ($(this).is(':checked')) {
      amen[$(this).data('id')] = $(this).data('name'); // if checked, add to amen
    } else {
      delete amen[$(this).data('id')]; // if not, delete from amen
    }
    $('div.amenities h4').text(Object.values(amen).join(', ')); // display amen list
  }
  );
});
