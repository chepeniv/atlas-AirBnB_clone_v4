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
    const check = data['status'];
    if (check === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });
});
