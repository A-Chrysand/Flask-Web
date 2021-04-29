//utf-8

window.onload = function () {
    $("#lg_input_text").val("eusername");
    $("#lg_input_psw").val('epassword');
    $("#rg_input_name").val("123131dfdf");
    $("#rg_input_email").val("dfcecaecsef@qweqwe.cdc");
    $("#rg_input_password").val("123123123");
    $("#rg_input_repassword").val("123123123");
}

function logincheck() {
    var string = $("#lg_input_text").val();
    var passwd = $("#lg_input_psw").val();
    var login_mingwen = string + '/' + passwd
    var login_sendout = Generate.Cipher_Num(login_mingwen);
    //ORG $.post("/js_post/"+ip, data_to_backend, function(data){alert("success "+data)} );
    $.post("/login_js_post/" + login_sendout, function (data) {
            if (data == 'success') {
                window.location.href = "\home";
            } else if (data == 'usernotfound') {
                alert("用户名不存在");
            } else if (data == 'passwderr') {
                alert("密码错误");
            }

        }
    )
}

function register() {
    var read_username = $("#rg_input_name").val();
    var read_email = $("#rg_input_email").val();
    var read_passwd = $("#rg_input_password").val();
    var read_ckpasswd = $("#rg_input_repassword").val();

    if (read_username == "") {
        alert("请输入用户名");
        return;
    } else if (read_email == "") {
        alert("请输入邮箱");
        return;
    } else if (read_passwd == "") {
        alert("请输入密码");
        return;
    } else if (read_ckpasswd == "") {
        alert("请输入确认密码");
        return;
    } else if (read_passwd != read_ckpasswd) {
        alert("输入的密码与确认密码不一致！");
        return;
    } else if (read_passwd.length < 6) {
        alert("输入的密码过短");
        return;
    } else {
        register_js_post(read_username, read_passwd, read_email);
    }
}

function register_js_post(send_username, send_passwd, send_email) {
    var register_mingwen = send_username + '/' + send_passwd + '/' + send_email;
    var register_sendout = Generate.Cipher_Num(register_mingwen);
    $.post("/register_js_post/" + register_sendout, function (data) {
        if (data == 'registersuccess') {
            alert("注册成功");
            window.location.href = "\home";
        } else if (data == 'registerfail') {
            alert("注册失败");
        } else if (data == 'registererror') {
            alert("服务器错误，注册失败");
        } else if (data == 'userregisted') {
            alert("用户名已被注册");
        } else if (data == 'mailregisted') {
            alert("邮箱已被注册");
        }

    });


}


/*      currentuser.xuehao = read_username;
        currentuser.name = read_email;
        currentuser.password = read_passwd;
        currentuser.banji = regpgClass;
        currentuser.age = regpgAge;
        currentuser.banjistr = $("#ClassSelectBox").find(":selected").html();
        currentuser.sex = regpgsex;
        userjson.visualuser[userjson_length] = currentuser;
        alert("注册成功！\n将跳转到主页");
        saveNopennewpage();*/