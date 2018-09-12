//====Slide in display=====


// debounce function by https://davidwalsh.name/javascript-debounce-function
function debounce(func, wait, immediate) {
  var timeout;
  return function() {
    var context = this, args = arguments;
    var later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
};

const slider = document.querySelectorAll('.slide-in');
function checkSlide(e){
  slider.forEach(slide => {
    const slideInAt = (window.scrollY + window.innerHeight) - slide.scrollHeight / 2;
    const sliderBottom = slide.offsetTop + slide.scrollHeight;
    const halfRevealed = slideInAt > slide.offsetTop;
    const isntScrolled = window.scrollY < sliderBottom;
    if(halfRevealed && isntScrolled) {
      slide.classList.add('active');
    } else {
      slide.classList.remove('active')
    }
  })
}
// window.addEventListener('scroll', debounce(checkSlide))
window.onload(debounce(checkSlide));
