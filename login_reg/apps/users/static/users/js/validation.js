$(document).ready(function(){
    $('#email-reg').keyup(function() {
        var data = $('#reg-form').serialize()
        $.ajax({
            method: "POST",
            url: "/email",
            data: data
        })
        .done(function(res){
            $('#email-msg').html(res)
        })
    })
})