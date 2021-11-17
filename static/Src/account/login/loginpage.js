var animatetime = 300;
var animatetime_hide = 50;
var animatetime_show = 500;
var animatecounter = 0;
var rightoffset = 0;


function createBundle(id, color, strwid) {
	if (strwid == null) {
		strwid = 10;
	}
	var wid = parseInt(($(".stars:eq(" + id + ")").css('width')).slice(0, -2));
	var l = parseInt(($(".stars:eq(" + id + ")").css('left')).slice(0, -2));
	var h = parseInt(($(".stars:eq(" + id + ")").css('bottom')).slice(0, -2));
	l += wid / 2 - strwid / 2;
	h += wid / 2
	$("#stars").append('<div id="bundle" style="background-color:' + color + ';width: ' + strwid + 'px;position: absolute;bottom: 0;left: ' + l + 'px;height:' + h + 'px;"></div>')
}

function jumptoIndex() {
	window.location.href = "\\";
	return false;
}


function dispWindow() {
	document.getElementById('tankuang').style.display = "";
}
function HideWindow(synth) {
	if (synth == 'x')
		$('#tankuang').css('display', "none")
	else if (synth == 'yes') {
		$("#Register_bottomtab #checkinfoinput").attr('checked', 'checked')
		$('#tankuang').css('display', "none")
	}
}




function changetologin() {
	if (animatecounter) {
		$("#text_leftarrow").hide(animatetime_hide);
		$("#text_denglu").animate({
			left: '+=' + animatemovement + 'px',
			fontSize: "3.5rem"
		}, animatetime).css("cursor", "default");
		$("#text_zhuce").animate({
			right: '-=' + (animatemovement - rightoffset) + 'px',
			fontSize: "1rem"
		}, animatetime).css("cursor", "pointer");
		$("#text_rightarrow").show(animatetime_show);

		$("#Register_bottomtab").hide(300);
		$("#Login_bottomtab").show(300);
		animatecounter++;
	}

}

function changetoregister() {
	if (!animatecounter) {
		$("#text_rightarrow").hide(animatetime_hide);
		$("#text_zhuce").animate({
			right: '+=' + (animatemovement - rightoffset) + 'px',
			fontSize: "3.5rem"
		}, animatetime).css("cursor", "default");
		$("#text_denglu").animate({
			left: '-=' + animatemovement + 'px',
			fontSize: "1rem"
		}, animatetime).css("cursor", "pointer");
		$("#text_leftarrow").show(animatetime_show);

		$("#Login_bottomtab").hide(300);
		$("#Register_bottomtab").show(300);
		animatecounter--;
	}
}
