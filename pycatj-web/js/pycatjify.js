$(function () {
    $('#convert_btn').click(function () {
        var data = {}
        data["pycatj_data"] = JSON.parse($('#in_form').val())
        // todo: add root input element
        // data["root"] = "POST"
        console.log(data)
        var body = JSON.stringify(data)
        $.ajax({
            url: "https://us-central1-pycatj.cloudfunctions.net/pycatjify",
            contentType: "application/json",
            data: body,
            dataType: "json",
            type: 'POST',
            success: function (response) {
                $('#out_form').val(response.data)
            }
        });
    });
});