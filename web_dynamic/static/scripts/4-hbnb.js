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

  // select state feedback and data caching
  let selectedState = {};
  $('.stateItem').click(function () {
    const thisState = {};
    const state = $(this);
    const stateId = state.attr('data-id');
    const stateName = state.attr('data-name');
    $('.selectedItem').removeClass('selectedItem');

    let oldStateId = Object.keys(selectedState);
    oldStateId = oldStateId[0];
    if (oldStateId !== stateId) {
      state.parent().addClass('selectedItem');
      selectedCity = {};
      thisState[stateId] = stateName;
      selectedState = thisState;
      $('.locations div h4').text(stateName);
      $('.locations div h4').css({ 'font-weight': 'bold' });
    } else {
      selectedState = {};
      $('.locations div h4').text('');
    }
  });

  // selected city feedback and data caching
  let selectedCity = [];
  $('.cityItem').click(function () {
    const thisCity = {};
    const city = $(this);
    const cityId = city.attr('data-id');
    const cityName = city.attr('data-name');
    $('.selectedItem').removeClass('selectedItem');

    let oldCityId = Object.keys(selectedCity);
    oldCityId = oldCityId[0];
    if (oldCityId !== cityId) {
	  city.addClass('selectedItem');
      selectedState = {};
      thisCity[cityId] = cityName;
      selectedCity = thisCity;
      $('.locations div h4').text(cityName);
      $('.locations div h4').css({ 'font-weight': 'normal' });
    } else {
	  selectedCity = {};
      $('.locations div h4').text('');
	}
  });

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

    // flash the button when clicked
    setTimeout(function () {
      button.addClass('search:active');
    }, 1);

    const amenityKeys = Object.keys(amenities);
    const cityKey = Object.keys(selectedCity);
    const stateKey = Object.keys(selectedState);

    // send request
    $.ajax({
      url: 'http://localhost:5001/api/v1/places_search/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        amenities: amenityKeys,
        cities: cityKey,
        states: stateKey
      }),

      // construct places from response
      success: function (places) { buildPlacesHtml(places); },
      error: function (error) {
        console.error('Error fetching places:', error);
      }
    });
  });
});
