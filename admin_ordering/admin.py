import inspect
import json

from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.helpers import InlineAdminFormSet
from django.contrib.admin.options import BaseModelAdmin, InlineModelAdmin
from django.core import checks
from js_asset import JS


__all__ = ("OrderableAdmin",)


class OrderableAdmin(BaseModelAdmin):
    ordering_field = "ordering"
    ordering_field_hide_input = False
    ordering_field_renumber_on_load = False
    extra = 0

    @property
    def media(self):
        if not isinstance(self, InlineModelAdmin):
            # Editable change list
            context = {
                "field": self.ordering_field,
                "fieldHideInput": self.ordering_field_hide_input,
                "renumberOnLoad": self.ordering_field_renumber_on_load,
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
                "renumberOnLoad": self.ordering_field_renumber_on_load,
                "prefix": helper.formset.prefix,
                "stacked": isinstance(self, admin.StackedInline),
                "tabular": isinstance(self, admin.TabularInline),
            }

        return super().media + forms.Media(
            css={
                "all": [
                    "admin_ordering/jquery-ui.min.css",
                    "admin_ordering/admin_ordering.css",
                ]
            },
            js=[
                "admin/js/jquery.init.js",
                "admin_ordering/jquery-ui.min.js",
                JS(
                    "admin_ordering/admin_ordering.js",
                    {
                        "class": "admin-ordering-context",
                        "data-context": json.dumps(context),
                    },
                ),
            ],
        )

    def check(self, **kwargs):
        errors = super().check(**kwargs)
        if "admin_ordering" not in settings.INSTALLED_APPS:
            errors.append(
                checks.Error(
                    '"admin_ordering" must be in INSTALLED_APPS.',
                    obj=self.__class__,
                    id="admin_ordering.E001",
                )
            )
        ordering = self.model._meta.ordering
        if list(ordering)[:1] != [self.ordering_field]:
            errors.append(
                checks.Warning(
                    f"The ordering of {self.model._meta.label} is {ordering}, but {self.__class__.__name__} uses {self.ordering_field!r}. This is inconsistent and potentially broken.",
                    obj=self.__class__,
                    id="admin_ordering.W004",
                    hint="Check that ordering_field is set if you're using a descending ordering.",
                )
            )
        return errors
