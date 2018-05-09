(function ($) {
    $(document).ready(function () {
        var time = $("id_time_slot");
        time.onchange = function (event) { alert(time.selectedIndex); };
    })
})(django.jQuery);