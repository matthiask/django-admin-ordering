============
Contributing
============

Running the test app
====================

Run `pip install .` to install dependencies.
The `tests` directory contains a Django app that uses admin_ordering. To set it up:

- run its migrations: `python manage.py migrate`
- create a superuser: `python manage.py createsuperuser`
- run the server: `python manage.py runserver`
- access the admin at `http://127.0.0.1:8000/admin/` and log in with the superuser.


Submission guidelines
=====================

If you are creating a pull request, fork the repository and make any changes
in your own feature branch.

Write and run tests.


Code of Conduct
===============

This project adheres to the
`Open Code of Conduct <http://todogroup.org/opencodeofconduct/#FeinCMS/dev@feinheit.ch>`_.
By participating, you are expected to honor this code.
