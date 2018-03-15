from __future__ import absolute_import, unicode_literals

import json

from django import forms
from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin, InlineModelAdmin
from django.core.exceptions import ImproperlyConfigured

from js_asset import JS


__all__ = ('OrderableAdmin',)


def get_default_formset_prefix(parent_model, model, fk_name):
    # Mostly lifted from django/forms/models.py
    try:
        from django.db.models.fields.related import RelatedObject

        return RelatedObject(
            parent_model,
            model,
            model._meta.get_field(fk_name),
        ).get_accessor_name().replace('+', '')

    except ImportError:
        pass

    # Newer versions of Django
    fk = model._meta.get_field(fk_name)
    rel = fk.remote_field if hasattr(fk, 'remote_field') else fk.rel
    return rel.get_accessor_name(model=model).replace('+', '')


class OrderableAdmin(BaseModelAdmin):
    ordering_field = 'ordering'
    ordering_field_hide_input = False
    extra = 0

    @property
    def media(self):
        if not isinstance(self, InlineModelAdmin):
            context = {
                'field': self.ordering_field,
                'fieldHideInput': self.ordering_field_hide_input,
            }
        else:
            if not self.fk_name:
                raise ImproperlyConfigured(
                    '%r requires a `fk_name` -- we are too dumb/lazy to'
                    ' determine it ourselves. Thanks!' % (self.__class__))

            context = {
                'field': self.ordering_field,
                'fieldHideInput': self.ordering_field_hide_input,
                'prefix': get_default_formset_prefix(
                    self.parent_model, self.model, self.fk_name),
                'stacked': isinstance(self, admin.StackedInline),
                'tabular': isinstance(self, admin.TabularInline),
            }

        return super(OrderableAdmin, self).media + forms.Media(
            css={'all': (
                'admin_ordering/admin_ordering.css',
            )},
            js=[
                'admin_ordering/jquery-ui-1.11.4.custom.min.js',
                JS('admin_ordering/admin_ordering.js', {
                    'class': 'admin-ordering-context',
                    'data-context': json.dumps(context),
                }),
            ],
        )
