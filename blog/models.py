from django.db import models
from django.utils import timezone
from .validators import lnglat_validator, min_length_validator, MinLengthValidator


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,
        validators=[min_length_validator(4)],
        verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.',
        validators=[min_length_validator(10)])
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

