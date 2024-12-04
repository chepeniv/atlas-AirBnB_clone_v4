#!/usr/bin/node
/* global $ */

$(function () {
  // provides a blueprint determining how html for a place is built
  function buildPlace (place) {
    const placeHtml = `
<article>
<h2>${place.name}</h2>
<div class="price_by_night">$${place.price_by_night}</div>
<div class="information">
    <div class="info_box">
        <div class="max_guest"></div>
        <div class="icon_desc">Guests: ${place.max_guest}</div>
    </div>

    <div class="info_box">
        <div class="number_rooms"></div>
        <div class="icon_desc">Bedrooms: ${place.number_rooms}</div>
    </div>

    <div class="info_box">
        <div class="number_bathrooms"></div>
        <div class="icon_desc">Bathrooms: ${place.number_bathrooms}</div>
    </div>
</div>

<div class="details">
    <div class="user">
        <b>Owner</b>: ${place.owner}
    </div>
    <div class="description">${place.description}</div>
</div>
</article>`;
    return placeHtml;
  }

  // constructs the html for each place fetched
  function buildPlacesHtml (places) {
    $('section.places').empty();
    for (const place of places) {
      const articlePlaces = buildPlace(place);
      $('section.places').append(articlePlaces);
    }
  }

  // filter bar feedback based on checked amenities
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

  // checks whether api server is running
  $.get('http://localhost:5001/api/v1/status/', function (data, stat) {
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });

  // populates the homepage with places upon initiation
  $.ajax({
    url: 'http://localhost:5001/api/v1/places_search',
    type: 'POST',
    contentType: 'application/json',
    data: '{}',
    success: function (places) { buildPlacesHtml(places); },
    error: function (error) {
      console.error('Error fetching places:', error);
    }
  });

  // search button behavior
  $('button').click(function () {
    const button = $(this);
    const checkedAmenities = [];

    // flash the button when clicked
    setTimeout(function () {
      button.addClass('search:active');
    }, 1);

    // collect the amenity_ids of each checked item
    // amenities variable might be better suited here
    $('.popover li input:checked').each(function () {
      const amenityID = $(this).attr('data-id');
      checkedAmenities.push(amenityID);
    });

    // send request
    $.ajax({
      url: 'http://localhost:5001/api/v1/places_search/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ amenities: checkedAmenities }),

      // construct places from response
      success: function (places) { buildPlacesHtml(places); },
      error: function (error) {
        console.error('Error fetching places:', error);
      }
    });
  });
});
