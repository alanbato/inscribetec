
(function ($) {
    function check_empalme() {
        var classroom = $("#id_classroom").val();
        var slot = $("#id_time_slot").val();
        $.ajax({
            url: ("/inscript/check_classroom/" + classroom + "/" + slot),
            type: "GET",
            data: null,
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                if (data.invalid == true) {
                    $("select#id_time_slot").after('<p style="color: red;">Horario ocupado en ese salón</p>');
                }
                else {
                    console.log("valid classroom!");
                }
            },
            error: function (err) {
                console.log("Error on ajax response");
            },
        }
        );
    }
    $(document).ready(function () {
        var time = $("#id_time_slot")
        time.on("input", check_empalme);
    })
})(django.jQuery);