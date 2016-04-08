from __future__ import absolute_import, unicode_literals

import json

from django import forms
from django.contrib.admin.options import BaseModelAdmin
from django.forms.utils import flatatt
from django.templatetags.static import static
from django.utils.html import format_html, mark_safe


__all__ = ('OrderableAdmin',)


class OrderableAdmin(BaseModelAdmin):
    ordering_field = 'ordering'

    @property
    def media(self):
        media = forms.Media()
        media.add_css({'all': (
            'admin_ordering/admin_ordering.css',
        )})
        media.add_js((
            'admin_ordering/jquery-ui-1.11.4.custom.min.js',
            JS('admin_ordering/admin_ordering.js', {
                'id': 'admin-ordering-context',
                'data-context': json.dumps({
                    'field': self.ordering_field,
                }),
            }),
        ))
        return media


class JS(object):
    """
    Use this to insert a script tag via ``forms.Media`` containing additional
    attributes (such as ``id`` and ``data-*`` for CSP-compatible data
    injection.)::

        media.add_js([
            JS('asset.js', {
                'id': 'asset-script',
                'data-the-answer': '"42"',
            }),
        ])

    The rendered media tag (via ``{{ media.js }}`` or ``{{ media }}`` will
    now contain a script tag as follows, without line breaks::

        <script type="text/javascript" src="/static/asset.js"
            data-answer="&quot;42&quot;" id="asset-script"></script>

    The attributes are automatically escaped. The data attributes may now be
    accessed inside ``asset.js``::

        var answer = document.querySelector('#asset-script').dataset.answer;
    """
    def __init__(self, js, attrs):
        self.js = js
        self.attrs = attrs

    def startswith(self, _):
        # Masquerade as absolute path so that we are returned as-is.
        return True

    def __html__(self):
        return format_html(
            '{}"{}',
            static(self.js),
            mark_safe(flatatt(self.attrs)),
        ).rstrip('"')
