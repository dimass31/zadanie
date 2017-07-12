$(document).ready(function () {
    var form = $('#forma');
    form.on('submit', function (e) {
        e.preventDefault();
        var string = submit_btn.data("string")
    })
});

 function basketUpdating(string){
        var data = {};
        data.string = string;
        var csrf_token = $('#forma [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
             },
             error: function(){
                 console.log("error")
             }
        })

}