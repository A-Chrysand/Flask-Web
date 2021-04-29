window.onload = function () {
    $("#lg_input_text").val("eusername");
    $("#lg_input_psw").val('epassword');
}

function logincheck() {
    let string = $("#lg_input_text").val();
    let passwd = $("#lg_input_psw").val();
    var mingwen = string + '/' + passwd
    var sendout = Generate.Cipher_Num(mingwen);
    //data_to_backend = { 'sendout': $(this).parent().prev().text() };
    //console.log(data_to_backend);
    //ORG $.post("/js_post/"+ip, data_to_backend, function(data){alert("success "+data)} );
    $.post("/js_post/" + sendout, function (data) {
    });
    sendout = ""
    mingwen = ""
}

function register() {
    alert("还没有做注册服务");
}
