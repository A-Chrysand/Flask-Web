function AnnouncementPage(strings) {
    var encodedstrings = URLencode(strings, sessionStorage.getItem("file_currentuser"));
    window.open("/home/announcement/" + encodedstrings);
}
function URLencode(string1, string2) {
    var EncodeString = "";
    // @ts-ignore
    EncodeString = Generate.Cipher_Num(string1 + '/' + string2);
    return EncodeString;
}
