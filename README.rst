==============================================================================
django-admin-ordering -- Orderable change lists and inlines done right^Wsimple
==============================================================================

.. image:: https://travis-ci.org/matthiask/django-admin-ordering.svg?branch=master
    :target: https://travis-ci.org/matthiask/django-admin-ordering

Steps
=====

0. Have a model ordered by an integer field.
1. Install ``django-admin-ordering`` and add ``admin_ordering`` to
   ``INSTALLED_APPS``.
2. Inherit ``admin_ordering.admin.OrderableAdmin`` in your own
   ``ModelAdmin`` and ``StackedInline``/``TabularInline`` subclasses and
   set ``ordering_field`` to a field name of the ordering integer field.
   Also set ``fk_name`` to the parent foreign key if you want orderable
   inlines. Do absolutely nothing if you want an orderable changelist.
3. Ensure that the field is displayed in the change form if you define
   fieldsets yourself, or is contained in ``list_editable`` for change lists.
4. Report any bugs you find (patches welcome)!

Limitations
===========

- Newly created inlines are not automatically assigned a good ordering
  value. This could be easily fixed for Django 1.9 by handling the
  ``formset:added`` signal.
- Only one inline can use this app per model right now.
- ``OrderableAdmin`` can be used both for inlines and parents, but this
  also means that you cannot register a model directly with
  ``OrderableAdmin``.
