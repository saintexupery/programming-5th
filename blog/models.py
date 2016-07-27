import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    author = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

