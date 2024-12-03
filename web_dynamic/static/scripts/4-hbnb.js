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

  $.ajax({
    url: 'http://localhost:5001/api/v1/places_search',
    type: 'POST',
    contentType: 'application/json',
    data: '{}', // empty dict
    cache: false,
    headers: {
      'Cache-Control': 'no-cache',
      'Pragma': 'no-cache'
    },
    success: function (places) {
      $('section.places').empty(); // clear the section

      for (const place of places) { // loop through the places
        const htmlPlaces = `
        <article>
          <div class="title_box">
            <h2>${place.name}</h2>
            <div class="price_by_night">$${place.price_by_night}</div>
          </div>
          <div class="information">
            <div class="max_guest">${place.max_guest} Guest${place.max_guest !== 1 ? 's' : ''}</div>
            <div class="number_rooms">${place.number_rooms} Bedroom${place.number_rooms !== 1 ? 's' : ''}</div>
            <div class="number_bathrooms">${place.number_bathrooms} Bathroom${place.number_bathrooms !== 1 ? 's' : ''}</div>
          </div>
          <div class="description">
            ${place.description}
          </div>
        </article>`;
        $('section.places').append(htmlPlaces); // append the article to the section
      }
    },
    error: function (error) {
      console.error('Error in fetching places:', error);
    }
    // send POST with content-type: application/json with an empty dict in
    // the body :
    // curl "http://0.0.0.0:5001/api/v1/places_search" -XPOST -H "Content-Type: application/json" -d '{}'`
    // loop through the request result and create an article in section.places
    // for each place extracted
    // owner tag in the place description may be removed
  });
});
