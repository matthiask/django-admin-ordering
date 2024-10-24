/* global django */
django.jQuery(($) => {
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

  $(".admin-ordering-context:not(.activated)")
    .addClass("activated")
    .each(function () {
      let $sortable
      let $sortableHandle
      const $sortableInputWrapper =
        '<span class="admin-ordering-field-input-wrapper"></span>'
      const $sortableHandleSelector = ".admin-ordering-field-input-wrapper"

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
        $sortableHandle = $sortable.find(`.field-${data.field}`)
        $sortableHandle.addClass("admin-ordering-field")
        if (data.fieldHideInput) {
          $sortableHandle.addClass("admin-ordering-field-hide-input")
        }
        $sortableHandle
          .find(`${inputFieldSelector}:not([type="hidden"])`)
          .wrap($sortableInputWrapper)
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
            updateOrdering($(`.dynamic-${data.prefix}`))
          },
          stop: (_event, ui) => {
            autoHorizontalOverflow()
            // reset ui item height
            ui.item.css("height", "auto")
          },
        })
      } else if (data.stacked) {
        $sortable = $(`#${data.prefix}-group`)
        $sortableHandle = $sortable.find(`.field-${data.field}`)
        $sortableHandle.addClass("admin-ordering-field")
        if (data.fieldHideInput) {
          $sortableHandle.addClass("admin-ordering-field-hide-input")
        }
        $sortableHandle
          .find(`${inputFieldSelector}:not([type="hidden"])`)
          .wrap($sortableInputWrapper)
        $sortable.sortable({
          items: ">.has_original,>>.has_original",
          handle: $sortableHandleSelector,
          start: (_event, ui) => {
            hideHorizontalOverflow()
            updatePlaceholderHeight(ui)
          },
          update: (_event, _ui) => {
            updateOrdering($(`.dynamic-${data.prefix}`))
          },
          stop: (_event, _ui) => {
            autoHorizontalOverflow()
          },
        })
      } else {
        $sortable = $("#result_list tbody")
        $sortableHandle = $sortable.find(`.field-${data.field}`)
        $sortableHandle.addClass("admin-ordering-field")
        if (data.fieldHideInput) {
          $sortableHandle.addClass("admin-ordering-field-hide-input")
        }
        if (!$sortableHandle.find("input").length) {
          return
        }
        $sortableHandle
          .find(`${inputFieldSelector}:not([type="hidden"])`)
          .wrap($sortableInputWrapper)
        $sortable.sortable({
          handle: $sortableHandleSelector,
          start: (_event, ui) => {
            hideHorizontalOverflow()
            updatePlaceholderHeight(ui)
          },
          update: (_event, _ui) => {
            updateOrdering($sortable.find("tr"))
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
