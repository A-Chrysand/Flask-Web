function Display_Common(target) {
    SetHTML05(target);
    SetCSS05();

}

function SetHTML05(target) {
    $(target).html("");
    var HTMLtext = '<div class=\"container\"><div class=\"form-floating mt-5\" style=\"max-width: 80%;margin-left:10%;\"><textarea class=\"form-control\" placeholder=\"Leave a comment here\" id=\"floatingTextarea\" style=\"height: 20rem;\"></textarea><label for=\"floatingTextarea\">Comments</label><button class=\"btn btn-info col-4 offset-4 col-lg-2 offset-lg-5 mt-3\" type=\"submit\">Submit</button></div></div>'
    ;
    $(target).append(HTMLtext);
}

function SetCSS05() {
    $('textarea').css('height', '20rem');
    $("label").css('color', 'black');
}