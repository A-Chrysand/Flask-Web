function Logout() {
	sessionStorage.removeItem("file_currentuser")
	window.location.href = "../login"
}

$("#colled_rightuser").trigger("click", function () {
	console.log('e')
	window.location.href = "/usercenter"
	return false
})

function SetLight() {
	console.log(11)
	let LightOff_Class = 'bg-dark text-light';
	let LightOn_Class = 'bg-light text-dark';
	if (sessionStorage.getItem("file_light") === "\"LightOFF\"") {
		$("body").removeClass(LightOff_Class).addClass(LightOn_Class)
		$("#div_wide_rightuser ul").removeClass(LightOff_Class).addClass(LightOn_Class)
		$("#div_wide_rightuser ul a").removeClass(LightOff_Class).addClass(LightOn_Class)
		$(".htmltext_username").removeClass('text-light').addClass('text-dark')
		$("#navbar_top_main").removeClass("navbar-dark navbg-dark").addClass("navbar-light navbg-light")
		$("#light_on").removeClass("active").addClass("disactive")
		$("#light_off").removeClass("disactive").addClass("active")
		sessionStorage.setItem("file_light", JSON.stringify("LightON"))//session保存数据到浏览器缓存
	} else {
		$("body").removeClass(LightOn_Class).addClass(LightOff_Class)
		$("#div_wide_rightuser ul").removeClass(LightOn_Class).addClass(LightOff_Class)
		$("#div_wide_rightuser ul a").removeClass(LightOn_Class).addClass(LightOff_Class)
		$(".htmltext_username").removeClass('text-dark').addClass('text-light')
		$("#navbar_top_main").removeClass("navbar-light navbg-light").addClass("navbar-dark navbg-dark")
		$("#light_off").removeClass("active").addClass("disactive")
		$("#light_on").removeClass("disactive").addClass("active")
		sessionStorage.setItem("file_light", JSON.stringify('LightOFF'))//session保存数据到浏览器缓存
	}
	/*
	if (sessionStorage.getItem("file_light") === "\"LightON\"") {
		$("body").removeClass(LightOn_Class).addClass(LightOff_Class);
		$("#wide_rightuser ul").removeClass(LightOn_Class).addClass(LightOff_Class);
		$("#wide_rightuser ul a").removeClass(LightOn_Class).addClass(LightOff_Class);
		$(".htmltext_username").removeClass('text-light').addClass('text-dark')
		$("#navbar_top_main").removeClass("navbar-light navbg-light").addClass("navbar-dark navbg-dark");
		$("#light_off").removeClass("active").addClass("disactive");
		$("#light_on").removeClass("disactive").addClass("active");
		sessionStorage.setItem("file_light", JSON.stringify("LightOFF"));//session保存数据到浏览器缓存
	} else if (sessionStorage.getItem("file_light") === "\"LightOFF\"") {
		$("body").removeClass(LightOff_Class).addClass(LightOn_Class)
		$("#wide_rightuser ul").removeClass(LightOff_Class).addClass(LightOn_Class)
		$("#wide_rightuser ul a").removeClass(LightOff_Class).addClass(LightOn_Class)
		$(".htmltext_username").removeClass('text-light').addClass('text-dark')
		$("#navbar_top_main").removeClass("navbar-dark navbg-dark").addClass("navbar-light navbg-light")
		$("#light_on").removeClass("active").addClass("disactive")
		$("#light_off").removeClass("disactive").addClass("active")
		sessionStorage.setItem("file_light", JSON.stringify("LightON"));//session保存数据到浏览器缓存
	} else { //定义第一次关灯
		$("body").removeClass(LightOn_Class).addClass(LightOff_Class)
		$("#wide_rightuser ul").removeClass(LightOn_Class).addClass(LightOff_Class)
		$("#wide_rightuser ul a").removeClass(LightOn_Class).addClass(LightOff_Class)
		$(".htmltext_username").removeClass('text-light').addClass('text-dark')
		$("#navbar_top_main").removeClass("navbar-light navbg-light").addClass("navbar-dark navbg-dark")
		$("#light_off").removeClass("active").addClass("disactive")
		$("#light_on").removeClass("disactive").addClass("active")
		sessionStorage.setItem("file_light", JSON.stringify('LightOFF'));//session保存数据到浏览器缓存
	}
	 */
}