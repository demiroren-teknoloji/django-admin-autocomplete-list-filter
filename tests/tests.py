from django.test import TestCase

from .models import Category, Tag

CATEGORY_TITLES = ['Python', 'Ruby', 'Golang', 'Bash']
TAG_NAMES = ['import', 'rake', 'interface', 'environment']


class DjaaTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.categories = []
        cls.tags = []

        for title in CATEGORY_TITLES:
            cls.categories.append(Category.objects.create(title=title))

        for name in TAG_NAMES:
            cls.tags.append(Tag.objects.create(name=name))

    def test_test_runner(self):
        self.assertEqual(1, 1)

    def test_category_model(self):
        for title in CATEGORY_TITLES:
            category = Category.objects.get(title=title)
            self.assertEqual(category.title, title)

    def test_tag_model(self):
        for name in TAG_NAMES:
            tag = Tag.objects.get(name=name)
            self.assertEqual(tag.name, name)
