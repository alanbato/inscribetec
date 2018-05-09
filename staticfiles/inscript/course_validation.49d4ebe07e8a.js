(function ($) {
    var time = $(document).getElementById("id_time_slot");
    time.onChange = function () { alert(time.selectedIndex) };
})(django.jQuery)