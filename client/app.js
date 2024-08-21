function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_suburb_names"; // Ensure this is the correct endpoint
  $.get(url, function(data, status) {
      console.log("got response from get_suburb_names request");
      if (data) {
          var suburbs = data.suburbs; // Make sure the key 'suburbs' matches the response structure
          var uiSuburb = document.getElementById("uiSuburb");
          $('#uiSuburb').empty(); // Ensure the dropdown is reset
          for (var i in suburbs) {
              var opt = new Option(suburbs[i]);
              $('#uiSuburb').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;

  
  window.onload = onPageLoad;

  function getBedValue() {
    return parseInt(document.getElementById('uiBedrooms').value);
}

function getBathValue() {
    return parseInt(document.getElementById('uiBathrooms').value);
}

function getGarageValue() {
    return parseInt(document.getElementById('uiGarage').value);
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
  // Get the values from the HTML elements
  var suburb = document.getElementById("uiSuburb").value;
  var bedrooms = getBedValue();
  var bathrooms = getBathValue();
  var garage = getGarageValue();
  var landArea = parseFloat(document.getElementById("uiLandArea").value);
  var floorArea = parseFloat(document.getElementById("uiFloorArea").value);
  var estPrice = document.getElementById("uiEstimatedPrice"); // Element to display estimated price

  var url = "http://127.0.0.1:5000/predict_home_price"; // Ensure this is the correct endpoint

  // Make the POST request
  $.post(url, {
      suburb: suburb,
      bedrooms: bedrooms,
      bathrooms: bathrooms,
      garage: garage,
      land_area: landArea,
      floor_area: floorArea
  }, function(data, status) {
      // Handle the response from the server
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "</h2>";
      console.log(status);
  }).fail(function(xhr, status, error) {
      console.error("Request failed:", status, error);
  });
}
