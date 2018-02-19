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

            $sortable = $('#' + data.prefix + '-group tbody');
            $sortable.sortable({
                items: '>.has_original',
                start: function(event, ui){
                    // hide body horizontal overflow while dragging row
                    $('body').css('overflow-x', 'hidden');

                    // set placeholder height equal to item height
                    ui.placeholder.height(ui.item.outerHeight());

                    // fix ui item appereance
                    ui.item.css('height', ui.item.outerHeight());
                },
                update: function(event, ui) {
                    updateOrdering($('.dynamic-' + data.prefix));
                },
                stop: function(event, ui){
                    // reset body horizontal overflow
                    $('body').css('overflow-x', 'auto');

                    ui.item.css('height', 'auto');
                }
            });

            // add custom css class to ordering field to customize it
            $sortable.find('.field-' + data.field).addClass('admin-ordering-field');

            // enforce row cells size while sorting rows
            $sortable.find('>tr').each(function(){
                $(this).mousedown(function(e){
                    $(this).find('td, th').each(function(){
                        $(this).css('width', $(this).width());
                    });
                }).mouseup(function(e){
                    $(this).find('td, th').each(function(){
                        $(this).css('width', 'auto');
                    });
                });
            });

        } else if (data.stacked) {

            $sortable = $('#' + data.prefix + '-group');
            $sortable.sortable({
                items: '>.has_original,>>.has_original',
                start: function(event, ui){
                    // hide body horizontal overflow while dragging row
                    $('body').css('overflow-x', 'hidden');

                    // set placeholder height equal to item height
                    ui.placeholder.height(ui.item.outerHeight());
                },
                update: function(event, ui) {
                    updateOrdering($('.dynamic-' + data.prefix));
                },
                stop: function(event, ui){
                    // reset body horizontal overflow
                    $('body').css('overflow-x', 'auto');
                }
            });

            // add custom css class to ordering field to customize it
            $sortable.find('.field-' + data.field).addClass('admin-ordering-field');

        } else {

            var $sortable = $('#result_list tbody');
            if (!$sortable.find('.field-' + data.field + ' input').length){
                return;
            }

            $sortable.sortable({
                // make the dragged row a little bit transparent
                start: function(event, ui){
                    // hide body horizontal overflow while dragging row
                    $('body').css('overflow-x', 'hidden');

                    // set placeholder height equal to item height
                    ui.placeholder.height(ui.item.outerHeight());
                },
                update: function(event, ui) {
                    updateOrdering($sortable.find('tr'));
                },
                stop: function(event, ui){
                    // reset body horizontal overflow
                    $('body').css('overflow-x', 'auto');
                }
            });

            // add custom css class to ordering field to customize it
            $sortable.find('.field-' + data.field).addClass('admin-ordering-field');

            // enforce row cells size while sorting rows
            $sortable.find('>tr').each(function(){
                $(this).mousedown(function(e){
                    $(this).find('td, th').each(function(){
                        $(this).css('width', $(this).width());
                    });
                }).mouseup(function(e){
                    $(this).find('td, th').each(function(){
                        $(this).css('width', 'auto');
                    });
                });
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
