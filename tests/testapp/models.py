from django.db import models

from admin_ordering.models import OrderableModel


class Parent1(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Child1(models.Model):
    parent = models.ForeignKey(
        Parent1, related_name="children", on_delete=models.CASCADE
    )
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Parent2(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Child2(models.Model):
    parent = models.ForeignKey(
        Parent2, related_name="children+", on_delete=models.CASCADE
    )
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return ""


class Parent3(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Child3(models.Model):
    parent = models.ForeignKey(Parent3, on_delete=models.CASCADE)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return ""


class Parent4(models.Model):
    title = models.CharField(max_length=100)
    _orderaaaaa = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Orderable(OrderableModel):
    pass
