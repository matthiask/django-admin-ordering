/* global django */
/* eslint indent:[2,4] */
/* eslint comma-dangle:[2,"never"] */
django.jQuery(function($){

    function updateOrdering(nodes) {
        var incOrdering = 10;
        var maxOrdering = (nodes.length * incOrdering);
        nodes.each(function(index) {
            var row = $(this);
            var rowOrdering = data.fieldDesc ? (maxOrdering - (incOrdering * index)) : (incOrdering * (index + 1));
            row.find('.field-' + data.field + ' input').val(rowOrdering);
            row.removeClass('row1 row2').addClass((index % 2) ? 'row2' : 'row1');
        });
    }

    $('.admin-ordering-context:not(.activated)').addClass('activated').each(function() {

        data = JSON.parse(this.getAttribute('data-context'));

        if (data.field.startsWith('-')) {
            data.field = data.field.substring(1);
            data.fieldDesc = true;
        } else {
            data.fieldDesc = false;
        }

        if (data.tabular) {
            $('#' + data.prefix + '-group tbody').sortable({
                items: '>.has_original',
                start: function(event, ui){
                    ui.placeholder.height(ui.item.height());
                },
                update: function(event, ui) {
                    updateOrdering($('.dynamic-' + data.prefix));
                }
            });
        } else if (data.stacked) {
            $('#' + data.prefix + '-group').sortable({
                items: '>.has_original,>>.has_original',
                start: function(event, ui){
                    ui.placeholder.height(ui.item.height());
                },
                update: function(event, ui) {
                    updateOrdering($('.dynamic-' + data.prefix));
                }
            });
        } else {
            var $tbody = $('#result_list tbody');
            if (!$tbody.find('.field-' + data.field + ' input').length)
                return;

            $tbody.sortable({
                start: function(event, ui){
                    ui.placeholder.height(ui.item.height());
                },
                update: function(event, ui) {
                    updateOrdering($tbody.find('tr'));
                }
            });
        }
    });

    if (data.tabular || data.stacked) {
        // Yay, Django 1.9 or better!
        $(document).on('formset:added', function newForm(event, row) {
            if (row.hasClass('dynamic-' + data.prefix)) {
                updateOrdering($('.dynamic-' + data.prefix));
            }
        });
    }
});
