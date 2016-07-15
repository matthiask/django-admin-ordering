/* global django */
/* eslint indent:[2,4] */
/* eslint comma-dangle:[2,"never"] */
django.jQuery(function($){
    var context = document.getElementById('admin-ordering-context');
    if (!context) return;

    var data = JSON.parse(context.getAttribute('data-context'));

    function updateOrdering(nodes) {
        nodes.each(function(index) {
            var row = $(this);
            row.find('.field-' + data.field + ' input').val(10 * (index + 1));
            row.removeClass('row1 row2').addClass((index % 2) ? 'row2' : 'row1');
        });
    }

    if (data.tabular) {
        $('#' + data.prefix + '-group tbody').sortable({
            update: function(event, ui) {
                updateOrdering($('.dynamic-' + data.prefix));
            }
        });
    } else if (data.stacked) {
        $('#' + data.prefix + '-group').sortable({
            items: '>.inline-related',
            update: function(event, ui) {
                updateOrdering($('.dynamic-' + data.prefix));
            }
        });
    } else {
        var $tbody = $('#result_list tbody');
        if (!$tbody.find('.field-' + data.field + ' input').length)
            return;

        $tbody.sortable({
            update: function(event, ui) {
                updateOrdering($tbody.find('tr'));
            }
        });
    }

    if (data.tabular || data.stacked) {
        // Yay, Django 1.9 or better!
        $(document).on('formset:added', function newForm(event, row) {
            if (row.hasClass('dynamic-' + data.prefix)) {
                updateOrdering($('.dynamic-' + data.prefix));
            }
        });
    }
});
