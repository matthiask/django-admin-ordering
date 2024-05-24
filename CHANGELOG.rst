.. _changelog:

Change log
==========

Next version
~~~~~~~~~~~~

- Added Python 3.11, 3.12 and Django 5.0.
- Switched to hatchling and ruff.
- Added a database index to the ordering field.


`0.17`_ (2023-05-05)
~~~~~~~~~~~~~~~~~~~~

.. _0.17: https://github.com/matthiask/django-admin-ordering/compare/0.16...0.17

- Fixed descending orderings.
- Added Django 4.2.
- Updated the bundled jQuery UI version.
- Changed the CSS and JavaScript to fix the handle selection. Do not mark the
  whole row as draggable. (This was never intentional.)
- Removed the ``mouseup`` and ``mousedown`` handler which fixed the width of
  cells during dragging. It seems to break file inputs inside sortables in
  Firefox. Breaking is worse than a potentially worse UI.


`0.16`_ (2022-09-20)
~~~~~~~~~~~~~~~~~~~~

.. _0.16: https://github.com/matthiask/django-admin-ordering/compare/0.15...0.16

- Stopped warning when ``ordering = ["-ordering"]``.
- Added Django 4.1.
- Raised the minimum version of django-js-asset to 2.0 for better compatibility
  with new Django versions.


`0.15`_ (2022-02-25)
~~~~~~~~~~~~~~~~~~~~

.. _0.15: https://github.com/matthiask/django-admin-ordering/compare/0.14...0.15

- Updated the bundled jQuery UI library to 1.12.1.
- Added a system check which verifies that ``admin_ordering`` is added to
  ``INSTALLED_APPS``.
- Added system checks for the ordering attribute of models.
- Added pre-commit.
- Raised the minimum version of Python to 3.8, Django to 3.2.
- Changed the ``formset:added`` handler for compatibility with Django 4.1.


`0.14`_ (2021-03-29)
~~~~~~~~~~~~~~~~~~~~

.. _0.14: https://github.com/matthiask/django-admin-ordering/compare/0.13...0.14

- Specified the default ordering by ``["ordering"]`` in the
  ``OrderableModel``.
- Started adding translations.
- Switched to a declarative setup.
- Switched from Travis CI to GitHub actions.
- Added comparison operator support to ``OrderableModel`` so that instances may
  be sorted in Python code.


`0.13`_ (2020-10-04)
~~~~~~~~~~~~~~~~~~~~

- Added Django 3.1 and Python 3.8 to the matrix.
- Added an abstract ``admin_ordering.models.OrderableModel`` model.


`0.12`_ (2019-11-18)
~~~~~~~~~~~~~~~~~~~~

- Added a notice to the README that using django-admin-ordering with
  filtered and/or paginated changelists may produce unexpected results.
- Checked compatibility with Django 2.2 and 3.0.
- Made the ordering field selector more specific to avoid an edge case.


`0.11`_ (2019-03-19)
~~~~~~~~~~~~~~~~~~~~

- Also reformatted ``setup.py`` using black and updated the Trove
  identifiers a bit.
- Added an explicit dependency on ``django.jQuery``.


`0.10`_ (2019-01-06)
~~~~~~~~~~~~~~~~~~~~

- Added automatic detection of formset's prefixes; now adding more than
  one inline per model is supported and explicitly specifying
  ``fk_name`` is not needed anymore.
- Reformatted the frontend code using prettier and added checking by
  ESLint.


`0.9`_ (2018-08-27)
~~~~~~~~~~~~~~~~~~~

- Fixed an accidental global ``data`` value in the JavaScript code.
- Added a default of ``extra=0`` for avoiding problems with empty but
  still invalid inlines.
- Fixed a duplicated handle when using ordering fields with callable
  defaults.
- Reformatted the code using black.


`0.8`_ (2018-01-25)
~~~~~~~~~~~~~~~~~~~

The following changes were contributed by Fabio Caccamo:

- Preserved the placeholder height when dragging starts.
- Added support for a descending ordering field, e.g. for a priority
  field.
- Added a handle for reordering items, ghosts of objects when dragging,
  and generally made the display of placeholders much nicer.
- Added support for hiding the ordering input field.


`0.7`_ (2018-01-25)
~~~~~~~~~~~~~~~~~~~

- Fixed the package to not install the test suite app when installing
  using pip. Thanks to Melvyn Sopacua for the contribution!
- Fixed an elusive bug with our formsets handling. Newly added content
  blocks have to be saved before they can be reordered.
- Extend item selector to work with stacked inlines on Django > 1.9.
  Thanks to Fabian Germann for the fix.
- Use tox for running tests and style checks.
- Fixed the package to work with the new ``forms.Media`` merging
  introduced in Django 2.0.


`0.6`_ (2017-05-15)
~~~~~~~~~~~~~~~~~~~

- Added Django@master to the test matrix.
- Reuse django-js-asset_ instead of bundling our own copy.


`0.5`_ (2016-11-05)
~~~~~~~~~~~~~~~~~~~

- Removed the limitation that only one inline can be orderable per model.


`0.4`_ (2016-07-15)
~~~~~~~~~~~~~~~~~~~

- Automatically fill in ordering values with inlines when using Django
  1.9 or better.


`0.3`_ (2016-07-07)
~~~~~~~~~~~~~~~~~~~

- Do not make changelists orderable when there are no matching inputs to
  be filled in.


`0.2`_ (2016-07-06)
~~~~~~~~~~~~~~~~~~~

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
.. _0.2: https://github.com/matthiask/django-admin-ordering/compare/0.1.1...0.2
.. _0.3: https://github.com/matthiask/django-admin-ordering/compare/0.2...0.3
.. _0.4: https://github.com/matthiask/django-admin-ordering/compare/0.3...0.4
.. _0.5: https://github.com/matthiask/django-admin-ordering/compare/0.4...0.5
.. _0.6: https://github.com/matthiask/django-admin-ordering/compare/0.5...0.6
.. _0.7: https://github.com/matthiask/django-admin-ordering/compare/0.6...0.7
.. _0.8: https://github.com/matthiask/django-admin-ordering/compare/0.7...0.8
.. _0.9: https://github.com/matthiask/django-admin-ordering/compare/0.8...0.9
.. _0.10: https://github.com/matthiask/django-admin-ordering/compare/0.9...0.10
.. _0.11: https://github.com/matthiask/django-admin-ordering/compare/0.10...0.11
.. _0.12: https://github.com/matthiask/django-admin-ordering/compare/0.11...0.12
.. _0.13: https://github.com/matthiask/django-admin-ordering/compare/0.12...0.13
