function Display_HeadPage(target) {
	SetHTML01(target);
	SetCSS01();
}

function SetHTML01(target) {
	$(target).html("");
	$(target).append("<div style=\"width: 100%;height: 300px; background-color: antiquewhite; color: black;\"><p id=\"banner\" style=\"margin:0px; text-align: center;\">广告位招租</p></div>");
}
function SetCSS01() {
	var font_size = document.body.clientWidth / 7;
	font_size > 200 ? font_size = 200 : font_size = font_size;
	document.getElementById("banner").style.fontSize = font_size.toString() + 'px';
}