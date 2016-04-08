from __future__ import absolute_import, unicode_literals

from django.contrib import admin

try:
    from django.urls import url
except ImportError:  # pragma: no cover
    from django.conf.urls import url


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
