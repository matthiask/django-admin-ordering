==============================================================================
django-admin-ordering -- Orderable change lists and inlines done right^Wsimple
==============================================================================

.. image:: https://github.com/matthiask/django-admin-ordering/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/matthiask/django-admin-ordering/
    :alt: CI Status

Please refer to the CI build linked above for the currently supported
combinations of Python and Django.


Installation
============

``pip install django-admin-ordering``, and add ``admin_ordering`` to
``INSTALLED_APPS``.


Usage
=====

First, you need a model ordered by an integer field. If you are happy
with a model where 1. the ordering field is called ``ordering`` and 2.
the ordering field is automatically initialized so that new objects are
ordered last you can also inherit the abstract
``admin_ordering.models.OrderableModel`` model. If you define your own ``class
Meta`` you should inherit ``OrderableModel.Meta`` so that the ``ordering``
attribute is set to the correct value:

.. code-block:: python

    from admin_ordering.models import OrderableModel

    class MyModel(OrderableModel):
        # ...

        class Meta(OrderableModel.Meta):
            # ...


Orderable change lists
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from admin_ordering.admin import OrderableAdmin

    @admin.register(MyModel)
    class MyModelAdmin(OrderableAdmin, admin.ModelAdmin):
        # The field used for ordering. Prepend a minus for reverse
        # ordering: "-ordering"
        # Doesn't have to be provided as long as you're using the default.
        # ordering_field = "ordering"

        # You may optionally hide the ordering field in the changelist:
        # ordering_field_hide_input = False

        # The ordering field can optionally be automatically renumbered when
        # the page loads. This may be useful if you have existing data which
        # isn't ordered yet.
        # ordering_field_renumber_on_load = False

        # The ordering field must be included both in list_display and
        # list_editable:
        list_display = ["name", "ordering"]
        list_editable = ["ordering"]


Orderable inlines
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from admin_ordering.admin import OrderableAdmin

    class MyModelTabularInline(OrderableAdmin, admin.TabularInline):
        model = MyModel

        # Same as above; "-ordering" is also allowed here:
        # ordering_field = "ordering"
        # ordering_field_hide_input = False
        # ordering_field_renumber_on_load = False

``OrderableAdmin`` comes with a default of ``extra = 0`` (no extra
empty inlines shown by default). It is strongly recommended to leave the
changed default as-is, because otherwise you'll end up with invalid
inlines just because you wanted to change the ordering.


Limitations
===========

- ``OrderableAdmin`` can be used both for inlines and parents, but this
  also means that you cannot register a model directly with
  ``OrderableAdmin``.
- Using django-admin-ordering with filtered or paginated lists may
  produce unexpected results. The recommendation right now is to set
  `list_per_page` to a bigger value and not reordering filtered
  changelists.
- Note that django-admin-ordering assigns ordering values in increments
  of 10, emphasizing that the ordering value should not have any
  significance apart from giving relative ordering to elements.
