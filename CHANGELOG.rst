.. _changelog:

Change log
==========

`Next version`_
~~~~~~~~~~~~~~~


`0.8.0`_ (2018-01-25)
~~~~~~~~~~~~~~~~~~~~~

The following changes were contributed by Fabio Caccamo:

- Preserved the placeholder height when dragging starts.
- Added support for a descending ordering field, e.g. for a priority
  field.
- Added a handle for reordering items, ghosts of objects when dragging,
  and generally made the display of placeholders much nicer.
- Added support for hiding the ordering input field.


`0.7.0`_ (2018-01-25)
~~~~~~~~~~~~~~~~~~~~~

- Fixed the package to not install the test suite app when installing
  using pip. Thanks to Melvyn Sopacua for the contribution!
- Fixed an elusive bug with our formsets handling. Newly added content
  blocks have to be saved before they can be reordered.
- Extend item selector to work with stacked inlines on Django > 1.9.
  Thanks to Fabian Germann for the fix.
- Use tox for running tests and style checks.
- Fixed the package to work with the new ``forms.Media`` merging
  introduced in Django 2.0.


`0.6.0`_ (2017-05-15)
~~~~~~~~~~~~~~~~~~~~~

- Added Django@master to the test matrix.
- Reuse django-js-asset_ instead of bundling our own copy.


`0.5.0`_ (2016-11-05)
~~~~~~~~~~~~~~~~~~~~~

- Removed the limitation that only one inline can be orderable per model.


`0.4.0`_ (2016-07-15)
~~~~~~~~~~~~~~~~~~~~~

- Automatically fill in ordering values with inlines when using Django
  1.9 or better.


`0.3.0`_ (2016-07-07)
~~~~~~~~~~~~~~~~~~~~~

- Do not make changelists orderable when there are no matching inputs to
  be filled in.


`0.2.0`_ (2016-07-06)
~~~~~~~~~~~~~~~~~~~~~

- Added a testsuite.


`0.1.1`_ (2016-04-08)
~~~~~~~~~~~~~~~~~~~~~

Initial public version.


.. _Django: https://www.djangoproject.com/
.. _django-js-asset: https://pypi.python.org/pypi/django-js-asset
.. _flake8: https://pypi.python.org/pypi/flake8
.. _isort: https://pypi.python.org/pypi/isort
.. _tox: https://tox.readthedocs.io/

.. _0.1.1: https://github.com/matthiask/django-admin-ordering/commit/be8c5581c4
.. _0.2.0: https://github.com/matthiask/django-admin-ordering/compare/0.1.1...0.2.0
.. _0.3.0: https://github.com/matthiask/django-admin-ordering/compare/0.2.0...0.3.0
.. _0.4.0: https://github.com/matthiask/django-admin-ordering/compare/0.3.0...0.4.0
.. _0.5.0: https://github.com/matthiask/django-admin-ordering/compare/0.4.0...0.5.0
.. _0.6.0: https://github.com/matthiask/django-admin-ordering/compare/0.5.0...0.6.0
.. _0.7.0: https://github.com/matthiask/django-admin-ordering/compare/0.6.0...0.7.0
.. _0.8.0: https://github.com/matthiask/django-admin-ordering/compare/0.7.0...0.8.0
.. _Next version: https://github.com/matthiask/django-admin-ordering/compare/0.8.0...master
