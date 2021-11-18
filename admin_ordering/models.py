from functools import total_ordering

from django.core import checks
from django.db import models
from django.db.models import Max
from django.utils.translation import gettext_lazy as _


@total_ordering
class OrderableModel(models.Model):
    ordering = models.PositiveIntegerField(_("ordering"), default=0)

    class Meta:
        abstract = True
        ordering = ["ordering"]

    def save(self, *args, **kwargs):
        if not self.ordering:
            max = self.__class__._default_manager.aggregate(m=Max("ordering"))["m"]
            self.ordering = 10 + (max or 0)
        super().save(*args, **kwargs)

    save.alters_data = True

    def __lt__(self, other):
        return (
            self.ordering < other.ordering if isinstance(other, type(self)) else False
        )

    @classmethod
    def check(cls, **kwargs):
        errors = super().check(**kwargs)
        if not cls._meta.ordering:
            errors.append(
                checks.Error(
                    'The ordering of "%s" is undefined.' % cls._meta.label,
                    obj=cls,
                    id="admin_ordering.E002",
                    hint='Make the inner Meta class inherit OrderableModel.Meta.',
                )
            )
        elif cls._meta.ordering[0] != "ordering":
            errors.append(
                checks.Warning(
                    '"%s" isn\'t ordered by the ordering field.' % cls._meta.label,
                    obj=cls,
                    id="admin_ordering.W003",
                    hint='Make the inner Meta class inherit OrderableModel.Meta.',
                )
            )
        return errors
