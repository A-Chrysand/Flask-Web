let Generate = {
	Jingdu: 2,
	PreChip: function (mingwen) {
		let pi: number[] = this.CreatePi();
		let time = new Date();
		let day: number = time.getDay();
		if (day < 7 && day != 0) {
			day += 1;
		} else {
			day = 8
		}
		let minute: number = time.getMinutes();

		let miwen: string[] = [];
		let miwenstr: string = "";
		let temp;
		// var asciicode = new Array();

		for (let i = 0; i < mingwen.length; i++) {
			//asciicode[i] = parseInt(mingwen[i].charCodeAt()) + " ";
			temp = parseFloat((((parseInt(mingwen[i].charCodeAt()) + pi[i]) + Math.pow(day, 2) - minute + 233) * 2.236).toString());
			miwen.push(temp.toFixed(this.Jingdu));
			miwenstr += ((miwen[i]).toString().slice(0, 3) + (miwen[i].toString().slice(4, 4 + this.Jingdu)));
		}
		//console.log("明文:           " + mingwen);
		//console.log("Ascii:          " + asciicode);
		//console.log("密文int array:  " + miwen);
		//console.log("密文String(" + miwenstr.length + "): " + miwenstr);
		//console.log({miwen, miwenstr});
		return {miwen, miwenstr};
	},
	Cipher_Ascii: function (mingwen) {
		let transfer = this.PreChip(mingwen);
		//var miwen = transfer["miwen"];
		let miwenstr = transfer["miwenstr"];
		let sendout = new Array();
		let sendoutstr: string = "";
		for (var i = 0; i < miwenstr.length; i += 2) {
			if (miwenstr[i + 1] != null) {
				sendout.push(String.fromCharCode(parseInt(miwenstr[i] + miwenstr[i + 1])));
				sendoutstr += (String.fromCharCode(parseInt(miwenstr[i] + miwenstr[i + 1])));
			} else {

				sendout.push(parseInt(miwenstr[miwenstr.length - 1]));
				sendoutstr += (parseInt(miwenstr[miwenstr.length - 1]));
			}
		}
		//console.log("发送Array:      " + sendout);
		//console.log("发送String:       " + sendoutstr);
		//$("#text2").html(sendout);
	},

	Cipher_Num: function (mingwen) {
		let pi: number[] = this.CreatePi();
		let transfer = this.PreChip(mingwen);
		let miwen = transfer["miwen"];
		//var miwenstr = transfer["miwenstr"];

		//console.log(pi);
		//console.log(miwen);
		//console.log(miwenstr);
		let sendout: string[] = [];
		let sendoutstr: string = "";
		for (var i = 0; i < miwen.length; i++) {
			sendout.push((parseFloat(miwen[i]) + pi[i]).toFixed(this.Jingdu).toString());
			//console.log(sendout[i]);
			sendoutstr += ((sendout[i]).toString().slice(0, 3) + (sendout[i].toString().slice(4, 4 + this.Jingdu)));
		}
		//$("#text3").html(sendoutstr);
		return sendoutstr;
		//console.log("发送Array:      " + sendout);
		//console.log("发送String:       " + sendoutstr);
	},
	CreatePi: function () {
		let pi_char = ((Math.PI).toString()).split('');
		//console.log(pi_char)
		let pi_num: number[] = []
		let last: number[] = [2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9]
		for (let i: number = 0, j: number = 0; i < 40; i++) {
			if (i != 1 && i < 16) {
				pi_num.push(parseInt(pi_char[i]))
			} else if (i > 16) {
				pi_num.push(last[j])
				j++
			} else {
				pi_num[i] = 6
			}
		}
		pi_num = pi_num.concat(pi_num);
		return pi_num;
	}
}