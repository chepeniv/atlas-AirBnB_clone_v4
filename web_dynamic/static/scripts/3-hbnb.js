#!/usr/bin/node
/* global $ */

$(function () {
  const amenities = {};

  $('div.amenities input[type="checkbox"]').change(function () {
    const element = $(this);
    const dataId = element.attr('data-id');
    const dataName = element.attr('data-name');

    if (element.is(':checked')) {
      amenities[dataId] = dataName;
    } else {
      delete amenities[dataId];
    }

    const amenityValues = Object.values(amenities);
    $('div.amenities h4').text(amenityValues);
  });

  $.get('http://localhost:5001/api/v1/status/', function (data, stat) {
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });

  $.get('http://localhost:5001/api/v1/places_search/', function (data, stat) {
    // send POST with content-type: application/json with an empty dict in
    // the body :
    // curl "http://0.0.0.0:5001/api/v1/places_search" -XPOST -H "Content-Type: application/json" -d '{}'`
    // loop through the request result and create an article in section.places
    // for each place extracted
    // owner tag in the place description may be removed
  });
});
