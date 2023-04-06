  const carousel = document.querySelector('.carousel');
  const carouselInner = carousel.querySelector('.carousel-inner');
  const carouselItems = carousel.querySelectorAll('.carousel-item');
  const carouselItemWidth = carouselItems[0].offsetWidth;

  let currentIndex = 0;
  let startX = null;

  carouselInner.style.transform = `translateX(-${currentIndex * carouselItemWidth}px)`;

  carousel.addEventListener('touchstart', e => {
    startX = e.changedTouches[0].clientX;
  });

  carousel.addEventListener('touchend', e => {
    if (startX === null) return;

    const endX = e.changedTouches[0].clientX;
    const diffX = startX - endX;

    if (diffX > 0 && currentIndex < carouselItems.length - 1) {
      currentIndex++;
    } else if (diffX < 0 && currentIndex > 0) {
      currentIndex--;
    }

    carouselInner.style.transform = `translateX(-${currentIndex * carouselItemWidth}px)`;

    startX = null;
  });

  const prevBtn = carousel.querySelector('.prev');
  prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      carouselInner.style.transform = `translateX(-${currentIndex * carouselItemWidth}px)`;
    }
  });

  const nextBtn = carousel.querySelector('.next');
  nextBtn.addEventListener('click', () => {
    if (currentIndex < carouselItems.length - 1) {
      currentIndex++;
      carouselInner.style.transform = `translateX(-${currentIndex * carouselItemWidth}px)`;
    }
  });
