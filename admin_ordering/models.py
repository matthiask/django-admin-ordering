from functools import total_ordering

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
        super(OrderableModel, self).save(*args, **kwargs)

    save.alters_data = True

    def __lt__(self, other):
        return (
            self.ordering < other.ordering if isinstance(other, type(self)) else False
        )
