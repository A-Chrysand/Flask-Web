var homelocation = '/templates/apps/home.html';
function logincheck() {
	var username = $("#lg_input_text").val();
	var userpasswd = $("#lg_input_psw").val();
	var login_mingwen = username + '/' + userpasswd;
	// @ts-ignore
	var login_sendout = Generate.Cipher_Num(login_mingwen);
	//ORG $.post("/js_post/"+ip, data_to_backend, function(data){alert("success "+data)} );
	saveNopennewpage(username);
	window.location.href = homelocation;
}
function register() {
	var read_username = $("#rg_input_name").val();
	var read_email = $("#rg_input_email").val();
	var read_passwd = $("#rg_input_password").val();
	var read_ckpasswd = $("#rg_input_repassword").val();
	if (read_username == "") {
		alert("请输入用户名");
		return;
	}
	else if (read_email == "") {
		alert("请输入邮箱");
		return;
	}
	else if (read_passwd == "") {
		alert("请输入密码");
		return;
	}
	else if (read_ckpasswd == "") {
		alert("请输入确认密码");
		return;
	}
	else if (read_passwd != read_ckpasswd) {
		alert("输入的密码与确认密码不一致！");
		return;
	}
	else if (typeof read_passwd !== "number" && read_passwd.length < 6) {
		alert("输入的密码过短");
		return;
	}
	else if (!$('#checkinfoinput').is(':checked')) {
		alert("请先阅读注意事项");
		return;
	}
	else {
		register_js_post(read_username, read_passwd, read_email);
	}
}
function register_js_post(send_username, send_passwd, send_email) {
	var register_mingwen = send_username + '/' + send_passwd + '/' + send_email;
	// @ts-ignore
	var register_sendout = Generate.Cipher_Num(register_mingwen);
	console.log(register_sendout);
	saveNopennewpage(send_username);
	alert("注册成功");
	window.location.href = homelocation;
}
function saveNopennewpage(save_username) {
	sessionStorage.setItem("file_currentuser", save_username); //session保存数据到浏览器缓存
}
