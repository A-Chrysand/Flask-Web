var animatetime = 300;
var animatetime_hide = 50;
var animatetime_show = 500;
var animatecounter = 0;
var rightoffset = 0;


function changetologin() {
	if (animatecounter) {
		$("#text_leftarrow").hide(animatetime_hide);
		$("#text_denglu").animate({ left: '+=' + animatemovement + 'px', fontSize: "3.5rem" }, animatetime).css("cursor", "default");
		$("#text_zhuce").animate({ right: '-=' + (animatemovement - rightoffset) + 'px', fontSize: "1rem" }, animatetime).css("cursor", "pointer");
		$("#text_rightarrow").show(animatetime_show);

		$("#Register_bottomtab").hide(300);
		$("#Login_bottomtab").show(300);
		animatecounter++;
	}

}

function changetoregister() {
	if (!animatecounter) {
		$("#text_rightarrow").hide(animatetime_hide);
		$("#text_zhuce").animate({ right: '+=' + (animatemovement - rightoffset) + 'px', fontSize: "3.5rem" }, animatetime).css("cursor", "default");
		$("#text_denglu").animate({ left: '-=' + animatemovement + 'px', fontSize: "1rem" }, animatetime).css("cursor", "pointer");
		$("#text_leftarrow").show(animatetime_show);

		$("#Login_bottomtab").hide(300);
		$("#Register_bottomtab").show(300);
		animatecounter--;
	}
}