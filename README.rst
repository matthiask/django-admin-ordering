==============================================================================
django-admin-ordering -- Orderable change lists and inlines done right^Wsimple
==============================================================================

.. image:: https://travis-ci.org/matthiask/django-admin-ordering.svg?branch=master
    :target: https://travis-ci.org/matthiask/django-admin-ordering

Please refer to the Travis CI build linked above for the currently
supported combinations of Python and Django.


Installation
============

``pip install django-admin-ordering``, and add ``admin_ordering`` to
``INSTALLED_APPS``.


Usage
=====

First, you need a model ordered by an integer field.


Orderable change lists
~~~~~~~~~~~~~~~~~~~~~~

::

    from admin_ordering.admin import OrderableAdmin

    @admin.register(MyModel)
    class MyModelAdmin(OrderableAdmin, admin.ModelAdmin):
        # The field used for ordering. Prepend a minus for reverse
        # ordering: '-order'
        ordering_field = 'order'

        # You may optionally hide the ordering field in the changelist:
        # ordering_field_hide_input = False

        # The ordering field must be included both in list_display and
        # list_editable:
        list_display = ('name', 'order', )
        list_editable = ('order', )


Orderable inlines
~~~~~~~~~~~~~~~~

::

    from admin_ordering.admin import OrderableAdmin

    class MyModelTabularInline(OrderableAdmin, admin.TabularInline):
        model = MyModel

        # You have to set the name of the parent foreign key yourself:
        fk_name = 'parent'

        # Same as above; '-order' is also allowed here:
        ordering_field = 'order'
        # ordering_field_hide_input = False


Limitations
===========

- Starting with Django 1.9 newly created inlines are automatically assigned
  a good ordering value. Earlier versions do not support the required
  ``formset:added`` signal.
- ``OrderableAdmin`` can be used both for inlines and parents, but this
  also means that you cannot register a model directly with
  ``OrderableAdmin``.
