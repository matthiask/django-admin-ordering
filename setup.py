#!/usr/bin/env python

from io import open
import os
from setuptools import setup, find_packages


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding='utf-8') as handle:
        return handle.read()


setup(
    name='django-admin-ordering',
    version=__import__('admin_ordering').__version__,
    description='Orderable change lists and inlines done right^Wsimple',
    long_description=read('README.rst'),
    author='Matthias Kestenholz',
    author_email='mk@feinheit.ch',
    url='https://github.com/matthiask/django-admin-ordering/',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(
        exclude=['tests']
    ),
    include_package_data=True,
    install_requires=[
        # 'Django>=1.9',
    ],
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    zip_safe=False,
    tests_require=[
        'Django',
        'coverage',
        'pytz',
    ],
    test_suite='testapp.runtests.runtests',
)
