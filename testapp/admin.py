from django.contrib import admin

from admin_ordering.admin import OrderableAdmin

from testapp import models


class Child1Inline(OrderableAdmin, admin.TabularInline):
    model = models.Child1
    fk_name = 'parent'
    ordering_field = 'ordering'


admin.site.register(
    models.Parent1,
    inlines=[
        Child1Inline,
    ],
)


class Child2Inline(OrderableAdmin, admin.TabularInline):
    model = models.Child2
    fk_name = 'parent'
    ordering_field = 'ordering'


admin.site.register(
    models.Parent2,
    inlines=[
        Child2Inline,
    ],
)


class Child3Inline(OrderableAdmin, admin.TabularInline):
    model = models.Child3
    fk_name = 'parent'
    ordering_field = 'ordering'


admin.site.register(
    models.Parent3,
    inlines=[
        Child3Inline,
    ],
)


class Parent4Admin(OrderableAdmin, admin.ModelAdmin):
    list_display = ('title', '_orderaaaaa')
    list_editable = ('_orderaaaaa',)
    ordering_field = '_orderaaaaa'


admin.site.register(
    models.Parent4,
    Parent4Admin,
)
