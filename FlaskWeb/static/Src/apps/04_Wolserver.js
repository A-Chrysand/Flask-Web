function Display_Wolserver(target) {
	SetHTML04(target);
	SetCSS04();
}


function SetHTML04(target) {
	$(target).html("");
	$(target).append("<div class=\"container\"><div class=\"offset-lg-3 col-lg-6 offset-md-2 col-md-8 col-sm-12\" style=\"border: red 1px solid; margin-top: 100px;\"><p style=\"text-align: center;font-size: 2rem;\">Wake On Lan 网络唤醒服务</p><div class=\"form-group\"><label for=\"rg_input_number\" class=\"control-label col-4\">目标Mac地址：</label><input type=\"text\" class=\"col-6\" id=\"rg_input_number\" placeholder=\"xx-xx-xx-xx-xx或xxxxxxxx\"></div><div class=\"form-group  pt-3\"><label for=\"rg_input_name\" class=\"control-label col-4\">目标ip地址：</label><input type=\"text\" class=\"col-6\" id=\"rg_input_name\" placeholder=\"xxx.xxx.xxx.xxx\"></div><div class=\"form-group  pt-3\"><label for=\"rg_input_password\" class=\"control-label col-4\">目标端口：</label><input type=\"text\" class=\"col-6\" id=\"rg_input_password\" placeholder=\"1-65535\"></div><div class=\"form-group  pt-3\"><label for=\"rg_input_repassword\" class=\"control-label col-4\">目标子网掩码：</label><input id=\"input_mask\" type=\"text\" class=\"col-5\" id=\"rg_input_repassword\" list=\"mask\"placeholder=\"xxx.xxx.xxx.xxx\"><datalist id=\"mask\"><option>255.0.0.0</option><option>255.255.0.0</option><option>255.255.255.0</option><option>255.255.255.255</option></datalist><button class=\"col-1\" onclick=\"cleantext()\">X</button><script>function cleantext() {$(\"#input_mask\").val(\"\");}</script></div><div class=\"form-group pt-4 pb-3\"><button class=\"btn btn-info col-3 offset-5\" type=\"button\" onclick=\"register()\">点火</button></div><style>.control-label {text-align: right;}</style></div></div>");
}

function SetCSS04() {


}