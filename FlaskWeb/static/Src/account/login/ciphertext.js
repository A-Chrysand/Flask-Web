var Generate = {
    jingdu: 2,
    PreChip: function (mingwen) {
        var pi = this.CreatePi();
        var time = new Date();
        var day = time.getDay() + 1;
        var minute = time.getMinutes();
        var miwen = [];
        var miwenstr = "";
        var temp;
        //var asciicode = new Array();
        for (var i = 0; i < mingwen.length; i++) {
            //asciicode[i] = parseInt(mingwen[i].charCodeAt()) + " ";
            temp = parseFloat((((parseInt(mingwen[i].charCodeAt()) + pi[i]) + Math.pow(day, 2) - minute + 233) * 2.236).toString());
            miwen.push(temp.toFixed(this.jingdu));
            //miwenstr += miwen[i];
            miwenstr += ((miwen[i]).toString().slice(0, 3) + (miwen[i].toString().slice(4, 4 + this.jingdu)));
        }
        //console.log("明文:           " + mingwen);
        //console.log("Ascii:          " + asciicode);
        //console.log("密文int array:  " + miwen);
        //console.log("密文String(" + miwenstr.length + "): " + miwenstr);
        //console.log({miwen, miwenstr});
        return { miwen: miwen, miwenstr: miwenstr };
    },
    Cipher_Ascii: function (mingwen) {
        var transfer = this.PreChip(mingwen);
        //var miwen = transfer["miwen"];
        var miwenstr = transfer["miwenstr"];
        var sendout = new Array();
        var sendoutstr = "";
        for (var i = 0; i < miwenstr.length; i += 2) {
            if (miwenstr[i + 1] != null) {
                sendout.push(String.fromCharCode(parseInt(miwenstr[i] + miwenstr[i + 1])));
                sendoutstr += (String.fromCharCode(parseInt(miwenstr[i] + miwenstr[i + 1])));
            }
            else {
                sendout.push(parseInt(miwenstr[miwenstr.length - 1]));
                sendoutstr += (parseInt(miwenstr[miwenstr.length - 1]));
            }
        }
        //console.log("转码Array:      " + sendout);
        //console.log("发送报文:       " + sendoutstr);
        //$("#text2").html(sendout);
    },
    Cipher_Num: function (mingwen) {
        var pi = this.CreatePi();
        var transfer = this.PreChip(mingwen);
        var miwen = transfer["miwen"];
        //var miwenstr = transfer["miwenstr"];
        //console.log(pi);
        //console.log(miwen);
        //console.log(miwenstr);
        var sendout = [];
        var sendoutstr = "";
        for (var i = 0; i < miwen.length; i++) {
            sendout.push((parseFloat(miwen[i]) + pi[i]).toFixed(this.jingdu).toString());
            //console.log(sendout[i]);
            sendoutstr += ((sendout[i]).toString().slice(0, 3) + (sendout[i].toString().slice(4, 4 + this.jingdu)));
        }
        //$("#text3").html(sendoutstr);
        return sendoutstr;
        //console.log("转码Array:      " + sendout);
        //console.log("发送报文:       " + sendoutstr);
    },
    CreatePi: function () {
        var pi_char = ((Math.PI).toString()).split('');
        //console.log(pi_char)
        var pi_num = [];
        var last = [2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9];
        for (var i = 0, j = 0; i < 40; i++) {
            if (i != 1 && i < 16) {
                pi_num.push(parseInt(pi_char[i]));
            }
            else if (i > 16) {
                pi_num.push(last[j]);
                j++;
            }
            else {
                pi_num[i] = 6;
            }
        }
        //console.log(pi_num)
        return pi_num;
    }
};
