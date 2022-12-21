window.addEventListener('scroll', () => {
    var header = document.querySelector('.navbar');
    header.classList.toggle('sticky', window.scrollY > 0);
});

window.addEventListener('scroll', function(){
    var scroll = document.querySelector('.scrollTop');
    scroll.classList.toggle('active', window.scrollY > 500)
});

function scrollToTop() {
    window.scrollTo({
      top: 0
    })
}

// Init Isotope
var $grid = $('.grid').isotope({
  // Options
});
// Filter items on button click
$('.filter-button-group').on( 'click', 'button', function() {
  var filterValue = $(this).attr('data-filter');
  $grid.isotope({ filter: filterValue });
});

// filter .metal AND .transition items
$grid.isotope({ filter: '.metal.transition' });

// filter .alkali OR .alkaline-earth items
$grid.isotope({ filter: '.alkali, .alkaline-earth' });

// Show all items
$grid.isotope({ filter: '*' });

function getFullscreen(element){
  if(element.requestFullscreen) {
      element.requestFullscreen();
    } else if(element.mozRequestFullScreen) {
      element.mozRequestFullScreen();
    } else if(element.webkitRequestFullscreen) {
      element.webkitRequestFullscreen();
    } else if(element.msRequestFullscreen) {
      element.msRequestFullscreen();
    }
}

var imagen = document.getElementById("miimagen");
imagen.addEventListener("dblclick", function(e){
  getFullscreen(this);
},false);