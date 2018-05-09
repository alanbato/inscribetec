$(document).ready(function () {
    var time = $("id_time_slot");
    time.onChange(function (event) { alert(time.selectedIndex); });
});