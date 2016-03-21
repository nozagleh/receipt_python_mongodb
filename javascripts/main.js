$(document).ready(function(){
	console.log('jQuery is up and running!');

	$('.menubtn').on('click',function(){
		/*Add better slide animation from the side*/
		$('#header').toggleClass('fixed');
		//showAndHideDiv('.menubar');
		showAndHideDiv('.menubar','display','block','none');
	});
	var showing = false;
	$('#addbtn').on('click',function(event) {
		showAndHideDiv('.addbox','display','block','none');
	});
});
var showing = false;
function showAndHideDiv(v,element,value1, value2){
	if (showing == false) {
		$(v).css(element, value1);
		showing = true;
	}else{
		$(v).css(element, value2);
		showing = false;
	};
}