$(document).ready(function() {
    
    $('#email').keyup(function() {
        var data = $('#reg-form').serialize();
        $.ajax({
            method: "POST",
            url: "/email",
            data: data
        })
        .done(function(res) {
            $('#email-msg').html(res)
        })
    })

    $('#username-reg').keyup(function(){
        var data = $('#reg-form').serialize()
        $.ajax({
            method: "POST",
            url: "/username",
            data: data
        })
        .done(function(res) {
            $('#username-msg').html(res)
        })
    })

})