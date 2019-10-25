![Python](https://img.shields.io/badge/python-3.5-green.svg)
![Python](https://img.shields.io/badge/python-3.6-green.svg)
![Python](https://img.shields.io/badge/python-3.7-green.svg)
![Django](https://img.shields.io/badge/django-2.1-green.svg)
![Django](https://img.shields.io/badge/django-2.2-green.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
[![PyPI version](https://badge.fury.io/py/django-admin-autocomplete-list-filter.svg)](https://badge.fury.io/py/django-admin-autocomplete-list-filter)

# django-admin-autocomplete-list-filter

Ajax autocomplete list filter helper for Django admin. Uses Django’s built-in
autocomplete widget! No extra package or install required!

![After](screenshots/demo.gif?v=2 "Widget in action...")

## Installation and Usage

```bash
$ pip install django-admin-autocomplete-list-filter
```

Add `djaa_list_filter` to `INSTALLED_APPS` in your `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djaa_list_filter',           
]
```

Now, let’s look at this example model:

```python
# models.py

from django.conf import settings
from django.db import models


class Post(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()
    tags = models.ManyToManyField(to='Tag', blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

```

We have 2 **ForeignKey** fields and one **ManyToManyField** to enable
autocomplete list filter feature on admin. All you need is to inherit from
`AjaxAutocompleteListFilterModelAdmin` which inherits from Django’s
`admin.ModelAdmin`.

Now we have an extra ModelAdmin method: `autocomplete_list_filter`. Uses 
Django Admin’s `search_fields` logic. You need to enable `search_fields`
in the related ModelAdmin. To enable completion on `Category` relation,
`CategoryAdmin` should have `search_fields` that’s it!

```python
from django.contrib import admin

from djaa_list_filter.admin import (
    AjaxAutocompleteListFilterModelAdmin,
)

from .models import Category, Post, Tag


@admin.register(Post)
class PostAdmin(AjaxAutocompleteListFilterModelAdmin):
    list_display = ('__str__', 'author', 'show_tags')
    autocomplete_list_filter = ('category', 'author', 'tags')

    def show_tags(self, obj):
        return ' , '.join(obj.tags.values_list('name', flat=True))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    ordering = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']

```

## Development

You are very welcome to contribute, fix bugs or improve this project. We
hope to help people who needs this feature. We made this package for
our company project. Good appetite for all the Django developers out there!

## License

This project is licensed under MIT

---

## Contributer(s)

* [Uğur "vigo" Özyılmazel](https://github.com/vigo) - Author, Maintainer
* [Can Adıyaman](https://github.com/canadiyaman) - Author, Maintainer
* [Erdi Mollahüseyinoğlu](https://github.com/erdimollahuseyin) - Author, Maintainer

---

## Contribute

All PR’s are welcome!

1. `fork` (https://github.com/demiroren-teknoloji/django-admin-autocomplete-list-filter/fork)
1. Create your `branch` (`git checkout -b my-features`)
1. `commit` yours (`git commit -am 'added killer options'`)
1. `push` your `branch` (`git push origin my-features`)
1. Than create a new **Pull Request**!

---

## TODO

- Add unit tests
- Improve JavaScript code :)

## Change Log

**2019-10-25**

- Remove f-string for older Python versions, will change this on 1.0.0 version

**2019-10-19**

- Bump version: 0.1.2
- Add Python 3.5 supports, thanks to [Peter Farrel](https://github.com/maestrofjp)
- Add animated gif :)
- Add future warning for f-strings

**2019-10-11**

- Add ManyToManyField support
- Initial release

**2019-10-07**

- Init repo...
