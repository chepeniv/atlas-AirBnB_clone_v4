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
    // send post with content-type: application/json
    // loop through the request result and create an article for each place
    // extracted in section.places
  });
});
