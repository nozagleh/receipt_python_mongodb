$(document).ready(function(){
	console.log('jQuery is up and running!');

	$('.menubtn').on('click',function(){
		/*Add better slide animation from the side*/
		showAndHideMenu('.menubar');
	});
});
var showing = false;
function showAndHideMenu(v){
	if (showing == false) {
		$(v).css('opacity', '1');
		showing = true;
	}else{
		$(v).css('opacity', '0');
		showing = false;
	};
}