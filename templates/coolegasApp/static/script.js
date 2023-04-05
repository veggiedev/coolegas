// Get the carousel element
const carousel = document.querySelector('#carousel-indicators');

// Initialize the swipe event listeners
let startX;
let endX;

carousel.addEventListener('touchstart', e => {
  startX = e.changedTouches[0].clientX;
});

carousel.addEventListener('touchend', e => {
  endX = e.changedTouches[0].clientX;
  if (startX > endX) {
    carousel.querySelector('.carousel-control-next').click();
  } else if (startX < endX) {
    carousel.querySelector('.carousel-control-prev').click();
  }
});
