//todo 长密码账号的转码问题

var Generate = new Object()
Generate.jingdu = 2
Generate.PreChip = function (mingwen) {
    var pi = this.CreatePi();
    //var asciicode = new Array();
    var miwen = new Array();
    var time = new Date();
    var day = time.getDay() + 1;
    var minute = time.getMinutes();
    //minute = 20;
    var miwenstr = "";
    var temp;

    for (var i = 0; i < mingwen.length; i++) {
        //asciicode[i] = parseInt(mingwen[i].charCodeAt()) + " ";
        temp = parseFloat(((parseInt(mingwen[i].charCodeAt()) + pi[i]) + Math.pow(day, 2) - minute + 233) * 2.236)
        miwen[i] = temp.toFixed(this.jingdu);
        //miwenstr += miwen[i];
        miwenstr += ((miwen[i]).toString().slice(0, 3) + (miwen[i].toString().slice(4, 4 + this.jingdu)));
    }
    //console.log("明文:           " + mingwen);
    //console.log("Ascii:          " + asciicode);
    //console.log("密文int array:  " + miwen);
    //console.log("密文String(" + miwenstr.length + "): " + miwenstr);
    console.log({miwen, miwenstr});
    return {miwen, miwenstr};
}
Generate.Cipher_Ascii = function (mingwen) {
    var transfer = this.PreChip(mingwen);
    //var miwen = transfer["miwen"];
    var miwenstr = transfer["miwenstr"];
    var sendout = new Array();
    var sendoutstr = "";
    for (var i = 0; i < miwenstr.length; i += 2) {
        if (miwenstr[i + 1] != null) {
            sendout.push(String.fromCharCode(parseInt(miwenstr[i] + miwenstr[i + 1])));
            sendoutstr += (String.fromCharCode(parseInt(miwenstr[i] + miwenstr[i + 1])));
        } else {

            sendout.push(parseInt(miwenstr[miwenstr.length - 1]));
            sendoutstr += (parseInt(miwenstr[miwenstr.length - 1]));
        }
    }
    //console.log("转码Array:      " + sendout);
    //console.log("发送报文:       " + sendoutstr);
    //$("#text2").html(sendout);
}
Generate.Cipher_Num = function (mingwen) {
    var pi = this.CreatePi()
    var transfer = this.PreChip(mingwen);
    var miwen = transfer["miwen"];
    //var miwenstr = transfer["miwenstr"];
    var sendout = new Array();
    var sendoutstr = "";
    //console.log(pi);
    var temp;
    //console.log(miwen);
    //console.log(miwenstr);
    for (var i = 0; i < miwen.length; i++) {
        sendout.push((parseFloat(miwen[i]) + pi[i]).toFixed(this.jingdu).toString());
        //console.log(sendout[i]);
        sendoutstr += ((sendout[i]).toString().slice(0, 3) + (sendout[i].toString().slice(4, 4 + this.jingdu)));
    }
    //$("#text3").html(sendoutstr);
    return sendoutstr;
    //console.log("转码Array:      " + sendout);
    //console.log("发送报文:       " + sendoutstr);
}
Generate.CreatePi = function () {

    var pi = ((Math.PI).toString()).split('');
    //pi.splice(1, 1);
    pi[1] = 6;
    for (var i = 0; i < pi.length; i++) {
        pi[i] = parseInt(pi[i]);
    }
    return pi;
}