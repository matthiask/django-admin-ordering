[![Build Status](https://travis-ci.org/matthiask/django-admin-ordering.svg?branch=master)](https://travis-ci.org/matthiask/django-admin-ordering)

# django-admin-ordering
Orderable change lists and inlines done right.

## Requirements
- Python 2.7, 3.4, 3.5, 3.6
- Django 1.7, 1.8, 1.9, 1.10, 1.11, 2.0

## Installation

1. Run ``pip install django-admin-ordering``
2. Add ``'admin_ordering'`` to ``settings.INSTALLED_APPS`` before custom applications
5. Restart your application server

## Usage

Just inherit from `admin_ordering.admin.OrderableAdmin` in your own ModelAdmin and StackedInline/TabularInline.

#### ModelAdmin:
```python
# ...
from admin_ordering.admin import OrderableAdmin

class MyModelAdmin(OrderableAdmin, admin.ModelAdmin):

    # [required] the field used for ordering
    # prepend a minus for reverse ordering: '-order'
    ordering_field = 'order'

    # [optional] if True the ordering field will be hidden
    ordering_field_hide_input = True

    # the ordering field must be included
    # both in list_display and list_editable
    list_display = ('name', 'order', )
    list_editable = ('order', )

admin.site.register(MyModel, MyModelAdmin)
```

#### StackedInline/TabularInline:
Inlines works exactly as normal model admins, but you must set `fk_name` to the parent foreign key field:

```python
class MyModelTabularAdmin(OrderableAdmin, admin.TabularInline):
    model = MyModel
    fk_name = 'parent'
    ordering_field = '-order'
    ordering_field_hide_input = True
```

```python
class MyModelStackedAdmin(OrderableAdmin, admin.StackedInline):
    model = MyModel
    fk_name = 'parent'
    ordering_field = '-order'
    ordering_field_hide_input = True
```

## Limitations

- Starting with Django 1.9 newly created inlines are automatically assigned
  a good ordering value. Earlier versions do not support the required
  `formset:added` signal.
- `OrderableAdmin` can be used both for inlines and parents, but this
  also means that you cannot register a model directly with
  `OrderableAdmin`.
