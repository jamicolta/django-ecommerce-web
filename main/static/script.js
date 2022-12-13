window.addEventListener('scroll', () => {
    var header = document.querySelector('.navbar');
    header.classList.toggle('sticky', window.scrollY > 0);
});

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