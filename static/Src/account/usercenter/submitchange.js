function submit_BaisicInfoChange_js_post() {
    var send_username = $("#input_username").val();
    var send_email = $("#input_email").val();
    var send_phone = $("#input_phone").val();
    var send_xuehao = $("#input_schoolNumber").val();
    var register_mingwen = send_username + '/' + send_email + '/' + send_phone + '/' + send_xuehao;
    // @ts-ignore
    var register_sendout = Generate.Cipher_Num(register_mingwen);
    $.post("/submit_BaisicInfoChange_js_post/" + register_sendout, function (data) {
        if (data == 'success') {
            saveNopennewpage(send_username);
            alert("修改成功");
        }
        else if (data == 'registerfail') {
            alert("注册失败");
        }
        else if (data == 'registererror') {
            alert("服务器错误，注册失败");
        }
        else if (data == 'userregisted') {
            alert("用户名已被注册");
        }
        else if (data == 'mailregisted') {
            alert("邮箱已被注册");
        }
        else if (data == 'passwdlengtherr') {
            alert("非法的密码长度!!!");
        }
    });
}
function submit_SecretInfoChange_js_post() {
    var send_username = sessionStorage.getItem("file_currentuser");
    var send_psw = $("#exampleInputPassword1").val();
    /*
    let send_q1 = $("#input_question1").val()
    let send_q2 = $("#input_question2").val()
    let send_q3 = $("#input_question3").val()
    todo 如何解决空值问题
    */
    var send_q1 = "123";
    var send_q2 = "1223";
    var send_q3 = "1233";
    //let register_mingwen: string = send_username + '/' + send_email + '/' + send_phone + '/' + send_xuehao;
    var register_mingwen = send_username + '/' + send_psw + '/' + send_q1 + '/' + send_q2 + '/' + send_q3;
    // @ts-ignore
    var register_sendout = Generate.Cipher_Num(register_mingwen);
    $.post("/submit_SecretInfoChange_js_post/" + register_sendout, function (data) {
        if (data == 'success') {
            saveNopennewpage(send_username);
            alert("修改成功");
        }
    });
}
function saveNopennewpage(save_username) {
    sessionStorage.setItem("file_currentuser", save_username); //session保存数据到浏览器缓存
}
function unlockinfo() {
    $("input.form-control").removeAttr("disabled");
}
