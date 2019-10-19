import random

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Category, Tag

CATEGORY_TITLES = ['Python', 'Ruby', 'Golang', 'Bash']
TAG_NAMES = ['import', 'rake', 'interface', 'environment']
USERNAMES = ['can', 'erdi', 'vigo', 'nobody']


class DjaaTestCase(TestCase):
    def setUp(self):
        self.categories = []
        self.tags = []
        self.users = []

        for title in CATEGORY_TITLES:
            self.categories.append(Category.objects.create(title=title))

        for name in TAG_NAMES:
            self.tags.append(Tag.objects.create(name=name))

        for username in USERNAMES:
            user = User.objects.create(
                username=username,
                password=str(random.random()),  # noqa: S311
                email='{username}@test.com'.format(username=username),
            )
            user.is_staff = True
            user.save()
            self.users.append(user)

    def test_category_model(self):
        for title in CATEGORY_TITLES:
            category = Category.objects.get(title=title)
            self.assertEqual(category.title, title)

    def test_tag_model(self):
        for name in TAG_NAMES:
            tag = Tag.objects.get(name=name)
            self.assertEqual(tag.name, name)

    def test_user_model(self):
        for username in USERNAMES:
            user = User.objects.get(username=username)
            self.assertEqual(user.username, username)
