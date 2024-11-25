/* global django */
django.jQuery(($) => {
  const $sortableInputWrapper =
  '<span class="admin-ordering-field-input-wrapper"></span>'
  const $sortableHandleSelector = ".admin-ordering-field-input-wrapper"

  function updatePlaceholderHeight(ui) {
    // set placeholder height equal to item height
    ui.placeholder.height(ui.item.outerHeight())
  }

  function hideHorizontalOverflow() {
    // hide body horizontal overflow while dragging row
    $("body").css("overflow-x", "hidden")
  }

  function autoHorizontalOverflow() {
    // reset body horizontal overflow
    $("body").css("overflow-x", "auto")
  }

  function setupSortableHandle($sortable, inputFieldSelector, rowsSelector, data, updateOrdering) {
    $sortableHandle = $sortable.find(`.field-${data.field}`)
    if (!$sortableHandle.find("input").length) {
      return $sortableHandle
    }

    $sortableHandle.addClass("admin-ordering-field")
    if (data.fieldHideInput) {
      $sortableHandle.addClass("admin-ordering-field-hide-input")
    }

    const $input = $sortableHandle.find(`${inputFieldSelector}:not([type="hidden"])`)
    $input.wrap($sortableInputWrapper)

    if (data.fieldUpDownArrows) {
      const $buttons = $('<span class="admin-ordering-field-up-down-buttons" />')
      const $upButton = $('<a class="admin-ordering-field-up-button" />')
      $upButton.click(function () {
        const $button = $(this)
        const $parentRow = $button.closest(rowsSelector)
        const $previousRow = $parentRow.prev(rowsSelector)
        if ($previousRow.length) {
          $parentRow.insertBefore($previousRow)
          updateOrdering($(rowsSelector))
        }
      })

      const $downButton = $('<a class="admin-ordering-field-down-button" />')
      $downButton.click(function () {
        const $button = $(this)
        const $parentRow = $button.closest(rowsSelector)
        const $nextRow = $parentRow.next(rowsSelector)
        if ($nextRow.length) {
          $parentRow.insertAfter($nextRow)
          setTimeout(() => {
            updateOrdering($(rowsSelector))
          }, 0)
        }
      })

      $buttons.append($upButton)
      $buttons.append($downButton)
      $input.before($buttons)
    }

    return $sortableHandle
  }

  $(".admin-ordering-context:not(.activated)")
    .addClass("activated")
    .each(function () {
      let $sortable
      let $sortableHandle

      const data = JSON.parse(this.getAttribute("data-context"))
      if (data.field.indexOf("-") === 0) {
        data.field = data.field.substring(1)
        data.fieldDesc = true
      } else {
        data.fieldDesc = false
      }

      const inputFieldSelector = `input[name$="-${data.field}"]`

      function updateOrdering(nodes) {
        const incOrdering = 10
        const maxOrdering = nodes.length * incOrdering
        nodes.each(function (index) {
          const row = $(this)
          const rowOrdering = data.fieldDesc
            ? maxOrdering - incOrdering * index
            : incOrdering * (index + 1)
          row.find(inputFieldSelector).val(rowOrdering)
          row.removeClass("row1 row2").addClass(index % 2 ? "row2" : "row1")
        })
      }

      if (data.tabular) {
        $sortable = $(`#${data.prefix}-group tbody`)
        const rowsSelector = `.dynamic-${data.prefix}`
        $sortableHandle = setupSortableHandle($sortable, inputFieldSelector, rowsSelector, data, updateOrdering)

        $sortable.sortable({
          items: ">.has_original",
          handle: $sortableHandleSelector,
          start: (_event, ui) => {
            hideHorizontalOverflow()
            updatePlaceholderHeight(ui)
            // fix ui item height
            ui.item.css("height", ui.item.outerHeight())
          },
          update: (_event, _ui) => {
            updateOrdering($(rowsSelector))
          },
          stop: (_event, ui) => {
            autoHorizontalOverflow()
            // reset ui item height
            ui.item.css("height", "auto")
          },
        })
      } else if (data.stacked) {
        $sortable = $(`#${data.prefix}-group`)
        const rowsSelector = `.dynamic-${data.prefix}`
        $sortableHandle = setupSortableHandle($sortable, inputFieldSelector, rowsSelector, data, updateOrdering)

        $sortable.sortable({
          items: ">.has_original,>>.has_original",
          handle: $sortableHandleSelector,
          start: (_event, ui) => {
            hideHorizontalOverflow()
            updatePlaceholderHeight(ui)
          },
          update: (_event, _ui) => {
            updateOrdering($(rowsSelector))
          },
          stop: (_event, _ui) => {
            autoHorizontalOverflow()
          },
        })
      } else {
        $sortable = $("#result_list tbody")
        const rowsSelector = "#result_list tbody tr"
        $sortableHandle = setupSortableHandle($sortable, inputFieldSelector, rowsSelector, data, updateOrdering)

        $sortable.sortable({
          handle: $sortableHandleSelector,
          start: (_event, ui) => {
            hideHorizontalOverflow()
            updatePlaceholderHeight(ui)
          },
          update: (_event, _ui) => {
            updateOrdering($(rowsSelector))
          },
          stop: (_event, _ui) => {
            autoHorizontalOverflow()
          },
        })
      }

      if (data.tabular || data.stacked) {
        $(document).on("formset:added", function newForm(event, $row) {
          if (event.detail?.formsetName) {
            // Django 4.1 or better!
            if ($(event.target).hasClass(`dynamic-${data.prefix}`)) {
              updateOrdering($(`.dynamic-${data.prefix}`))
            }
          } else {
            if ($row.hasClass(`dynamic-${data.prefix}`)) {
              updateOrdering($(`.dynamic-${data.prefix}`))
            }
          }
        })

        if (data.renumberOnLoad) {
          updateOrdering($(`.dynamic-${data.prefix}`))
        }
      } else if (data.renumberOnLoad) {
        updateOrdering($sortable.find("tr"))
      }
    })
})
