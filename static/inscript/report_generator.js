(function ($) {
    function courses_by() {
        var teacher = $("#courses_by_select").val();
        $.ajax({
            url: ("/inscript/courses_by/" + teacher),
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
        var btn1 = $("#courses_by_btn")
        bt1.on("click", courses_by);
    })

    function courses_by() {
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



    function courses_by() {
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




    function courses_by() {
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




    function courses_by() {
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



    function courses_by() {
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


// response = '<div class="col-sm-9">' +
//     '<h2>Materias registradas:</h2>' +
//     '<table class="table table-striped">' +
//     '<thead>' +
//     '<tr>' +
//     '<th>Clave de materia</th>' +
//     '<th>Nombre de materia</th>' +
//     '<th>Horas de laboratorio</th>' +
//     '</tr>' +
//     '</thead>' +
//     '<tbody>'
// response.forEach(subject => {
//     <tr>
//         <td>TC1003</td>
//         <td>Matemáticas Discretas</td>
//         <td>0</td>
//     </tr>
// });
//         </tbody >
//     </table >
// </div >
