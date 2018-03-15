/* global django */
/* eslint indent:[2,4] */
/* eslint comma-dangle:[2,"never"] */
django.jQuery(function($){

    function updatePlaceholderHeight(ui) {
        // set placeholder height equal to item height
        ui.placeholder.height(ui.item.outerHeight());
    }

    function hideHorizontalOverflow() {
        // hide body horizontal overflow while dragging row
        $('body').css('overflow-x', 'hidden');
    }

    function autoHorizontalOverflow() {
        // reset body horizontal overflow
        $('body').css('overflow-x', 'auto');
    }

    function enforceSortableRowsCellsSize(node) {
        // enforce row cells size while sorting rows
        node.find('>tr').each(function(){
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

    $('.admin-ordering-context:not(.activated)').addClass('activated').each(function() {

        var $sortable, $sortableHandle, $sortableInputWrapper = '<span class="admin-ordering-field-input-wrapper"></span>';

        var data = JSON.parse(this.getAttribute('data-context'));

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

        if (data.field.startsWith('-')) {
            data.field = data.field.substring(1);
            data.fieldDesc = true;
        } else {
            data.fieldDesc = false;
        }

        if (data.tabular) {

            $sortable = $('#' + data.prefix + '-group tbody');
            $sortableHandle = $sortable.find('.field-' + data.field);
            $sortableHandle.addClass('admin-ordering-field');
            if (data.fieldHideInput) {
                $sortableHandle.addClass('admin-ordering-field-hide-input');
            }
            $sortableHandle.find('input').wrap($sortableInputWrapper);
            $sortable.sortable({
                items: '>.has_original',
                handle: $sortableHandle,
                start: function(event, ui){
                    hideHorizontalOverflow();
                    updatePlaceholderHeight(ui);
                    // fix ui item height
                    ui.item.css('height', ui.item.outerHeight());
                },
                update: function(event, ui) {
                    updateOrdering($('.dynamic-' + data.prefix));
                },
                stop: function(event, ui){
                    autoHorizontalOverflow();
                    // reset ui item height
                    ui.item.css('height', 'auto');
                }
            });

            enforceSortableRowsCellsSize($sortable);

        } else if (data.stacked) {

            $sortable = $('#' + data.prefix + '-group');
            $sortableHandle = $sortable.find('.field-' + data.field);
            $sortableHandle.addClass('admin-ordering-field');
            if (data.fieldHideInput) {
                $sortableHandle.addClass('admin-ordering-field-hide-input');
            }
            $sortableHandle.find('input').wrap($sortableInputWrapper);
            $sortable.sortable({
                items: '>.has_original,>>.has_original',
                handle: $sortableHandle,
                start: function(event, ui){
                    hideHorizontalOverflow();
                    updatePlaceholderHeight(ui);
                },
                update: function(event, ui) {
                    updateOrdering($('.dynamic-' + data.prefix));
                },
                stop: function(event, ui){
                    autoHorizontalOverflow();
                }
            });

        } else {

            $sortable = $('#result_list tbody');
            $sortableHandle = $sortable.find('.field-' + data.field);
            $sortableHandle.addClass('admin-ordering-field');
            if (data.fieldHideInput) {
                $sortableHandle.addClass('admin-ordering-field-hide-input');
            }
            if (!$sortableHandle.find('input').length) {
                return;
            }
            $sortableHandle.find('input').wrap($sortableInputWrapper);
            $sortable.sortable({
                handle: $sortableHandle,
                start: function(event, ui){
                    hideHorizontalOverflow();
                    updatePlaceholderHeight(ui);
                },
                update: function(event, ui) {
                    updateOrdering($sortable.find('tr'));
                },
                stop: function(event, ui){
                    autoHorizontalOverflow();
                }
            });

            enforceSortableRowsCellsSize($sortable);
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
});
