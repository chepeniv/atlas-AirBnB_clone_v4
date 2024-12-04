#!/usr/bin/node
/* global $ */

$(function () {
  const amenities = {};

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
        <b>Owner</b>: John Doe
    </div>
    <div class="description">${place.description}</div>
</div>
</article>`;
    // user name not extracted
    return placeHtml;
  }

  function buildPlacesHtml (places) {
    $('section.places').empty();
    for (const place of places) {
      const articlePlaces = buildPlace(place);
      $('section.places').append(articlePlaces);
    }
  }

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
    data: '{}',

    cache: false,
    headers: {
      'Cache-Control': 'no-cache',
      Pragma: 'no-cache'
    },

    success: function (places) { buildPlacesHtml(places); },
    error: function (error) {
      console.error('Error fetching places:', error);
    }
  });

  $('button').click(function () {
    // flash the button when clicked
    $(this).removeClass('search:active');
    setTimeout(function () {
      $(this).addClass('search:active');
    }, 1);

    const checkedAmenities = [];
    $('div.amenities input[type="checkbox"]').each(function () {
      if ($(this).is(':checked')) {
        checkedAmenities.push($(this).data('id'));
      }
    });

    $.ajax({
      url: 'http://localhost:5001/api/v1/places_search/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ amenities: checkedAmenities }),
      success: function (places) { buildPlacesHtml(places); },
      error: function (error) {
        console.error('Error fetching places:', error);
      }
    });
  });
});
