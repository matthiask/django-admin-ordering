/* global django */
/* eslint indent:[2,4] */
/* eslint comma-dangle:[2,"never"] */
django.jQuery(function($){
    var context = document.getElementById('admin-ordering-context');
    if (!context) return;

    var data = JSON.parse(context.getAttribute('data-context'));

    if (data.tabular) {
        $('#' + data.prefix + '-group tbody').sortable({
            update: function(event, ui) {
                $('.dynamic-' + data.prefix).each(function(index) {
                    var row = $(this);
                    row.find('.field-' + data.field + ' input').val(10 * (index + 1));
                    row.removeClass('row1 row2').addClass((index % 2) ? 'row2' : 'row1');
                });
            }
        });
    } else if (data.stacked) {
        $('#' + data.prefix + '-group').sortable({
            items: '>.inline-related',
            update: function(event, ui) {
                $('.dynamic-' + data.prefix).each(function(index) {
                    var row = $(this);
                    row.find('.field-' + data.field + ' input').val(10 * (index + 1));
                    row.removeClass('row1 row2').addClass((index % 2) ? 'row2' : 'row1');
                });
            }
        });
    } else {
        var $tbody = $('#result_list tbody');
        if (!$tbody.find('.field-' + data.field + ' input').length)
            return;

        $tbody.sortable({
            update: function(event, ui) {
                $tbody.find('tr').each(function(index) {
                    var row = $(this);
                    row.find('.field-' + data.field + ' input').val(10 * (index + 1));
                    row.removeClass('row1 row2').addClass((index % 2) ? 'row2' : 'row1');
                });
            }
        });
    }
});
