from django.db import models

__all__ = ['Post', 'Category', 'Tag']


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='posts')
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
