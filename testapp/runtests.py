from __future__ import absolute_import, unicode_literals

from coverage import Coverage

cov = Coverage()  # noqa
cov.start()  # noqa


import os
import sys
import django
from django.conf import settings


# Make testapp/content_editor importable
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        },
    },
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.admin',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sitemaps',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'testapp',
        'admin_ordering',
    ),
    STATIC_URL='/static/',
    SECRET_KEY='tests',
    ROOT_URLCONF='testapp.urls',
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    ),
    USE_TZ=True,
    LANGUAGES=(('en', 'English'), ('de', 'German')),
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }],
)

if hasattr(django, 'setup'):
    django.setup()


def runtests():
    from django.conf import settings
    from django.test.utils import get_runner

    test_runner = get_runner(settings)(verbosity=2, interactive=True)
    failures = test_runner.run_tests([])

    cov.stop()
    cov.report(
        include=['*/admin_ordering/*'],
        # omit=['*migrations*'],
    )
    if 'TRAVIS' not in os.environ:
        cov.html_report(include=['*/admin_ordering/*'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
