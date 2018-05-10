function courses_by() {
    var teacher = $("#courses_by_select").val();
    $.ajax({
        url: ("courses_by/" + teacher),
        type: "GET",
        data: null,
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            if (data.length >= 1) {
                element = ('<div class="col-sm-11">' +
                    '<h2>Grupos del profesor: ' + teacher + '</h2>' +
                    '<table class="table table-striped">' +
                    '<thead>' +
                    '<tr>' +
                    '<th>Clave de materia</th>' +
                    '<th>Grupo</th>' +
                    '<th>Horario</th>' +
                    '<th>Salón</th>' +
                    '<th>Idioma</th>' +
                    '<th>Honors</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>')
                for (let index = 0; index < data.length; index++) {
                    const course = data[index];
                    if (course.in_english) {
                        idioma = "Ingles";
                    } else {
                        idioma = "Español";
                    }
                    if (course.honors) {
                        honors = "Si";
                    } else {
                        honors = "No";
                    }
                    element += (
                        "<tr>" +
                        "<td>" + course.clave + "</td>" +
                        "<td>" + course.grupo + "</td>" +
                        "<td>" + course.horario + "</td>" +
                        "<td>" + course.salon + "</td>" +
                        "<td>" + idioma + "</td>" +
                        "<td>" + honors + "</td>" + "</tr>"
                    );
                }
                element += ("</tbody >" +
                    "</table >" +
                    "</div >"
                );
            }
            else {
                element = "<h2>Este maestro no tiene grupos asignados.</h2>";
            }
            $("div#reporte").empty()
            $("div#reporte").append(element)
        },
        error: function (err) {
            console.log("Error on ajax response");
        },
    }
    );
}

function courses_of() {
    var subject = $("#courses_of_select").val();
    $.ajax({
        url: ("courses_of/" + subject),
        type: "GET",
        data: null,
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            if (data.length >= 1) {
                element = ('<div class="col-sm-11">' +
                    '<h2>Grupos de la materia: ' + subject + '</h2>' +
                    '<table class="table table-striped">' +
                    '<thead>' +
                    '<tr>' +
                    '<th>Clave de materia</th>' +
                    '<th>Grupo</th>' +
                    '<th>Profesor</th>' +
                    '<th>Horario</th>' +
                    '<th>Salón</th>' +
                    '<th>Idioma</th>' +
                    '<th>Honors</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>')
                for (let index = 0; index < data.length; index++) {
                    const course = data[index];
                    if (course.in_english) {
                        idioma = "Ingles";
                    } else {
                        idioma = "Español";
                    }
                    if (course.honors) {
                        honors = "Si";
                    } else {
                        honors = "No";
                    }
                    element += (
                        "<tr>" +
                        "<td>" + course.clave + "</td>" +
                        "<td>" + course.grupo + "</td>" +
                        "<td>" + course.profesor + "</td>" +
                        "<td>" + course.horario + "</td>" +
                        "<td>" + course.salon + "</td>" +
                        "<td>" + idioma + "</td>" +
                        "<td>" + honors + "</td>" + "</tr>"
                    );
                }
                element += ("</tbody >" +
                    "</table >" +
                    "</div >"
                );
            }
            else {
                element = "<h2>No hay grupos para esta materia.</h2>";
            }
            $("div#reporte").empty();
            $("div#reporte").append(element);
        },
        error: function (err) {
            console.log("Error on ajax response");
        },
    }
    );
}

function classrooms_at() {
    var time = $("#classrooms_at_select").val();
    $.ajax({
        url: ("classrooms_at/" + time),
        type: "GET",
        data: null,
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            if (data.length >= 1) {
                element = ('<div class="col-sm-11">' +
                    '<h2>Salones disponibles en el horario: ' + time + '</h2>' +
                    '<table class="table table-striped">' +
                    '<thead>' +
                    '<tr>' +
                    '<th>Salón</th>' +
                    '<th>Capacidad</th>' +
                    '<th>Administrador</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>')
                for (let index = 0; index < data.length; index++) {
                    const room = data[index];
                    element += (
                        "<tr>" +
                        "<td>" + room.salon + "</td>" +
                        "<td>" + room.cap + "</td>" +
                        "<td>" + room.admin + "</td></tr>"
                    );
                }
                element += ("</tbody >" +
                    "</table >" +
                    "</div >"
                );
            }
            else {
                element = "<h2>No hay salones disponibles en este horario.</h2>";
            }
            $("div#reporte").empty();
            $("div#reporte").append(element);
        },
        error: function (err) {
            console.log("Error on ajax response");
        },
    }
    );
}

function teaching_at() {
    var time = $("#teaching_at_select").val();
    $.ajax({
        url: ("teaching_at/" + time),
        type: "GET",
        data: null,
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            if (data.length >= 1) {
                element = ('<div class="col-sm-11">' +
                    '<h2>Profesores enseñando en el horario: ' + time + '</h2>' +
                    '<table class="table table-striped">' +
                    '<thead>' +
                    '<tr>' +
                    '<th>Nómina</th>' +
                    '<th>Nombre</th>' +
                    '<th>Teléfono</th>' +
                    '<th>Correo</th>' +
                    '<th>Número de clases</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>')
                for (let index = 0; index < data.length; index++) {
                    const teacher = data[index];
                    element += (
                        "<tr>" +
                        "<td>" + teacher.id + "</td>" +
                        "<td>" + teacher.name + "</td>" +
                        "<td>" + teacher.phone + "</td>" +
                        "<td>" + teacher.email + "</td>" +
                        "<td>" + teacher.groups + "</td></tr>"
                    );
                }
                element += ("</tbody >" +
                    "</table >" +
                    "</div >"
                );
            }
            else {
                element = "<h2>No hay maestros enseñando en este horario.</h2>";
            }
            $("div#reporte").empty();
            $("div#reporte").append(element);
        },
        error: function (err) {
            console.log("Error on ajax response");
        },
    }
    );
}

function not_teaching_at() {
    var time = $("#not_teaching_at_select").val();
    $.ajax({
        url: ("not_teaching_at/" + time),
        type: "GET",
        data: null,
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            if (data.length >= 1) {
                element = ('<div class="col-sm-11">' +
                    '<h2>Profesores que no están enseñando en el horario: ' + time + '</h2>' +
                    '<table class="table table-striped">' +
                    '<thead>' +
                    '<tr>' +
                    '<th>Nómina</th>' +
                    '<th>Nombre</th>' +
                    '<th>Teléfono</th>' +
                    '<th>Correo</th>' +
                    '<th>Número de clases</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>')
                for (let index = 0; index < data.length; index++) {
                    const teacher = data[index];
                    element += (
                        "<tr>" +
                        "<td>" + teacher.id + "</td>" +
                        "<td>" + teacher.name + "</td>" +
                        "<td>" + teacher.phone + "</td>" +
                        "<td>" + teacher.email + "</td>" +
                        "<td>" + teacher.groups + "</td></tr>"
                    );
                }
                element += ("</tbody >" +
                    "</table >" +
                    "</div >"
                );
            }
            else {
                element = "<h2>Todos los maestros están enseñando en este horario.</h2>";
            }
            $("div#reporte").empty();
            $("div#reporte").append(element);
        },
        error: function (err) {
            console.log("Error on ajax response");
        },
    }
    );
}

function courses_at() {
    var day = $("#courses_at_day_select").val();
    var classroom = $("#courses_at_classroom_select").val();
    $.ajax({
        url: ("course_at/" + day + "/" + classroom),
        type: "GET",
        data: null,
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            if (data.length >= 1) {
                element = ('<div class="col-sm-11">' +
                    '<h2>Grupos de los ' + day + ' en el salón: ' + classroom + '</h2>' +
                    '<table class="table table-striped">' +
                    '<thead>' +
                    '<tr>' +
                    '<th>Clave de materia</th>' +
                    '<th>Grupo</th>' +
                    '<th>Profesor</th>' +
                    '<th>Horario</th>' +
                    '<th>Idioma</th>' +
                    '<th>Honors</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>')
                for (let index = 0; index < data.length; index++) {
                    const course = data[index];
                    if (course.in_english) {
                        idioma = "Ingles";
                    } else {
                        idioma = "Español";
                    }
                    if (course.honors) {
                        honors = "Si";
                    } else {
                        honors = "No";
                    }
                    element += (
                        "<tr>" +
                        "<td>" + course.clave + "</td>" +
                        "<td>" + course.grupo + "</td>" +
                        "<td>" + course.profesor + "</td>" +
                        "<td>" + course.horario + "</td>" +
                        "<td>" + idioma + "</td>" +
                        "<td>" + honors + "</td>" + "</tr>"
                    );
                }
                element += ("</tbody >" +
                    "</table >" +
                    "</div >"
                );
            }
            else {
                element = "<h2>No hay grupos ese día en ese salón.</h2>";
            }
            $("div#reporte").empty();
            $("div#reporte").append(element);
        },
        error: function (err) {
            console.log("Error on ajax response");
        },
    }
    );
}

$(document).ready(function () {
    var btn1 = $("#courses_by_btn");
    btn1.on("click", courses_by);
    var btn2 = $("#courses_of_btn");
    btn2.on("click", courses_of);
    var btn3 = $("#classrooms_at_btn");
    btn3.on("click", classrooms_at);
    var btn4 = $("#teaching_at_btn");
    btn4.on("click", teaching_at);
    var btn5 = $("#not_teaching_at_btn");
    btn5.on("click", not_teaching_at);
    var btn6 = $("#courses_at_btn");
    btn6.on("click", courses_at)
});