from __future__ import absolute_import, unicode_literals

import json

from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin, InlineModelAdmin
from django.core.exceptions import ImproperlyConfigured
from django.forms.utils import flatatt
from django.templatetags.static import static
from django.utils.html import format_html, mark_safe


__all__ = ('OrderableAdmin',)


class OrderableAdmin(BaseModelAdmin):
    ordering_field = 'ordering'

    def _get_default_formset_prefix(self):
        # Mostly lifted from django/forms/models.py

        if not self.fk_name:
            raise ImproperlyConfigured(
                '%r requires a `fk_name` -- we are too dumb/lazy to determine'
                ' it ourselves. Thanks!' % (self.__class__))

        try:
            from django.db.models.fields.related import RelatedObject

            return RelatedObject(
                self.parent_model,
                self.model,
                self.model._meta.get_field(self.fk_name),
            ).get_accessor_name().replace('+', '')

        except ImportError:
            pass

        # Newer versions of Django
        fk = self.model._meta.get_field(self.fk_name),
        rel = fk.remote_field if hasattr(fk, 'remote_field') else fk.rel
        return rel.get_accessor_name(model=self.model).replace('+', '')

    @property
    def media(self):
        media = super(OrderableAdmin, self).media
        media.add_css({'all': (
            'admin_ordering/admin_ordering.css',
        )})
        media.add_js((
            'admin_ordering/jquery-ui-1.11.4.custom.min.js',
            JS('admin_ordering/admin_ordering.js', {
                'id': 'admin-ordering-context',
                'data-context': json.dumps({
                    'field': self.ordering_field,
                    'model': '%s_%s' % (
                        self.model._meta.app_label,
                        self.model._meta.model_name,
                    ),
                    'stacked': isinstance(self, admin.StackedInline),
                    'tabular': isinstance(self, admin.TabularInline),
                    'prefix': (
                        self._get_default_formset_prefix()
                        if isinstance(self, InlineModelAdmin)
                        else ''),
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
