/* JavaScript Document */
jQuery(document).ready(function() {
    'use strict';

	/* image-carousel function by = owl.carousel.js */
	jQuery('.trending-stories').owlCarousel({
		loop:true,
		center:true,
		margin:40,
		nav:true,
		dots: false,
		navText: ['<i class="la la-long-arrow-left"></i>', '<i class="la la-long-arrow-right"></i>'],
		responsive:{
			0:{
				items:1,
			},
			480:{
				items:2,
				margin:20
			},			
			1024:{
				items:3
			},
			1200:{
				items:3
			},
			1400:{
				items:3
			}
		}
	})
	
	/* image-carousel function by = owl.carousel.js */
	jQuery('.header-blog-carousel').owlCarousel({
		loop:true,
		margin:20,
		nav:true,
		dots: false,
		navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
		responsive:{
			0:{
				items:1,
				margin:10,
				center: true,
				stagePadding: 30
			},
			480:{
				items:1,
				margin:10,
				center: true,
				stagePadding: 30
			},			
			1024:{
				items:3
			},
			1200:{
				items:4
			},
			1400:{
				items:4
			}
		}
	})
	
	/*  Blog post Carousel function by = owl.carousel.js */
	jQuery('.blog-carousel').owlCarousel({
		loop:true,
		autoplay:true,
		margin:30,
		nav:true,
		dots: false,
		navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:2
			},			
			991:{
				items:2
			},
			1000:{
				items:3
			}
		}
	})
	
	/* post Carousel function by = owl.carousel.js */
	jQuery('.post-carousel').owlCarousel({
		loop:true,
		autoplay:true,
		margin:0,
		nav:true,
		dots: true,
		navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:1
			},			
			991:{
				items:1
			},
			1000:{
				items:1
			}
		}
	})
	
	/*  Blog post Carousel function by = owl.carousel.js */
	jQuery('.post-slide').owlCarousel({
		loop:true,
		autoplay:true,
		margin:0,
		nav:true,
		autoplaySpeed: 1000,
		navSpeed: 1000,
		paginationSpeed: 1000,
		slideSpeed: 1000,
		dots: false,
		navText: ['<i class="la la-long-arrow-left"></i>', '<i class="la la-long-arrow-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:1
			},			
			991:{
				items:1
			},
			1000:{
				items:1
			}
		}
	})
	
	/*  Blog post Carousel function by = owl.carousel.js */
	jQuery('.post-slide1').owlCarousel({
		loop:true,
		autoplay:true,
		margin:30,
		center:true,
		nav:true,
		autoplaySpeed: 1000,
		navSpeed: 1000,
		paginationSpeed: 1000,
		slideSpeed: 1000,
		dots: false,
		navText: ['<i class="la la-long-arrow-left"></i>', '<i class="la la-long-arrow-right"></i>'],
		responsive:{
			0:{
				items:1,
				stagePadding: 15,
			},
			480:{
				items:1,
				stagePadding: 15
			},			
			991:{
				items:1
			},
			1000:{
				items:1.2,
			}
		}
	})
	
	/*  Blog post Carousel function by = owl.carousel.js */
	jQuery('.post-slide2').owlCarousel({
		loop:true,
		autoplay:true,
		margin:40,
		center:true,
		stagePadding: 40,
		nav:true,
		autoplaySpeed: 1000,
		navSpeed: 1000,
		paginationSpeed: 1000,
		slideSpeed: 1000,
		dots: false,
		navText: ['<i class="la la-long-arrow-left"></i>', '<i class="la la-long-arrow-right"></i>'],
		responsive:{
			0:{
				items:1,
				stagePadding: 15
			},
			480:{
				items:1
			},			
			991:{
				items:2
			},
			1000:{
				items:3,
			}
		}
	})
	/*  Blog post Carousel function by = owl.carousel.js */
	jQuery('.post-slide3').owlCarousel({
		loop:true,
		autoplay:true,
		margin:0,
		center:true,
		stagePadding: 0,
		nav:true,
		autoplaySpeed: 1000,
		navSpeed: 1000,
		paginationSpeed: 1000,
		slideSpeed: 1000,
		dots: false,
		navText: ['<i class="la la-long-arrow-left"></i>', '<i class="la la-long-arrow-right"></i>'],
		responsive:{
			0:{
				items:1,
			},
			480:{
				items:1
			},			
			991:{
				items:1
			},
			1000:{
				items:1,
			}
		}
	})
});
/* Document .ready END */