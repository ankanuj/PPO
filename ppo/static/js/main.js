const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
	$('#message').fadeOut('slow');
}, 3000);

$(window).scroll(function()
{
	$(".sildeanim").each(function()
	{
		var pos = $(this).offset().top;

		var winTop = $(window).scrollTop();
		if (pos < winTop + 600){
			$(this).addClass("slide");
		}
	});
});