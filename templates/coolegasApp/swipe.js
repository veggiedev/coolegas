{% load static %}

var pictures = [
    { image: '/static/images/picture1.jpg', name: 'John' },
    { image: '/static/images/picture2.jpg', name: 'Jane' },
    { image: '/static/images/picture3.jpg', name: 'Bob' },
    // add more pictures here
  ];
 




  /* Use JavaScript to generate the picture cards dynamically from the array of objects. You can use a for loop to loop through the array and create a new <div> element for each picture card. You can use the innerHTML property to set the contents of the card to the HTML markup you created in step 3.
  css
  Copy code
  // Example JavaScript code to generate picture cards */
  var cardContainer = document.querySelector('.card-container');
  
  for (var i = 0; i < pictures.length; i++) {
    var card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = '<img src="' + pictures[i].image + '" alt="' + pictures[i].name + '">' +
                     '<p>' + pictures[i].name + '</p>';
    cardContainer.appendChild(card);
  }