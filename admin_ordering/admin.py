from __future__ import absolute_import, unicode_literals

import inspect
import json

from django import forms
from django.contrib import admin
from django.contrib.admin.helpers import InlineAdminFormSet
from django.contrib.admin.options import BaseModelAdmin, InlineModelAdmin

from js_asset import JS


__all__ = ("OrderableAdmin",)


class OrderableAdmin(BaseModelAdmin):
    ordering_field = "ordering"
    ordering_field_hide_input = False
    extra = 0

    @property
    def media(self):
        if not isinstance(self, InlineModelAdmin):
            # Editable change list
            context = {
                "field": self.ordering_field,
                "fieldHideInput": self.ordering_field_hide_input,
            }
        else:
            # Find our helper.InlineAdminFormSet so that we may access
            # the formset instance and its prefix
            frame = inspect.currentframe()
            while frame:  # pragma: no branch
                helper = frame.f_locals.get("self")
                if isinstance(helper, InlineAdminFormSet):
                    break
                frame = frame.f_back
            del frame

            context = {
                "field": self.ordering_field,
                "fieldHideInput": self.ordering_field_hide_input,
                "prefix": helper.formset.prefix,
                "stacked": isinstance(self, admin.StackedInline),
                "tabular": isinstance(self, admin.TabularInline),
            }

        return super(OrderableAdmin, self).media + forms.Media(
            css={"all": ("admin_ordering/admin_ordering.css",)},
            js=[
                "admin/js/jquery.init.js",
                "admin_ordering/jquery-ui-1.11.4.custom.min.js",
                JS(
                    "admin_ordering/admin_ordering.js",
                    {
                        "class": "admin-ordering-context",
                        "data-context": json.dumps(context),
                    },
                ),
            ],
        )
