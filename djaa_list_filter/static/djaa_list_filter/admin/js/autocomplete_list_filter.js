function handle_querystring_and_redirect(querystring_value, qs_target_value, selection) {
    var required_queryset = [];
    if (querystring_value.length > 0) {
        for(const field_eq_value of querystring_value.split("&")){
            var [field, value] = field_eq_value.split("=");
            if (field != qs_target_value){
                required_queryset.push(field_eq_value)
            }
        }
    }
    if (selection.length > 0) {
        required_queryset.push(qs_target_value + "=" + selection);
    }
    window.location.href = "?" + required_queryset.join("&");
}

django.jQuery(document).ready(function(){
    django.jQuery(".ajax-autocomplete-select-widget-wrapper select").on('select2:unselect', function(e){
        var qs_target_value = django.jQuery(this).parent().data("qs-target-value");
        var querystring_value = django.jQuery(this).closest("form").find('input[name="querystring_value"]').val();
        handle_querystring_and_redirect(querystring_value, qs_target_value, "");
    });

    django.jQuery(".ajax-autocomplete-select-widget-wrapper select").on('change', function(e, choice){
        var selection = django.jQuery(e.target).val() || "";
        var qs_target_value = django.jQuery(this).parent().data("qs-target-value");
        var querystring_value = django.jQuery(this).closest("form").find('input[name="querystring_value"]').val();
        if(selection.length > 0){
            handle_querystring_and_redirect(querystring_value, qs_target_value, selection);
        }
    });
});
