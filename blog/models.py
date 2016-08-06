from django.db import models
from django.utils import timezone
from django.core.files import File
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from .validators import lnglat_validator, MinLengthValidator, phone_number_validator, ZipCodeValidator, get_file_path
from .fields import PhoneNumberField, PostCodeField
from .utils import square_image, thumbnail


class Post(models.Model):
    author = models.CharField(max_length=20,
        validators=[ZipCodeValidator(True)])
    title = models.CharField(max_length=100,
        validators=[MinLengthValidator(4)],
        verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.',
        validators=[MinLengthValidator(10)])
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)
    photo = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])
        #'blog.views.post_detail'이 작동하지 않는 이유는 url의 두 번째 인자가 문자열이 아닌 함수이기 때문이다.


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    author = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_number = PhoneNumberField()


class PostCode(models.Model):
    region = models.CharField(max_length=20)
    post_code = PostCodeField()

    def __str__(self):
        return self.post_code


class ZipCode(models.Model):
    city = models.CharField(max_length=20)
    road = models.CharField(max_length=20)
    dong = models.CharField(max_length=20)
    gu = models.CharField(max_length=20)
    code = models.CharField(max_length=7)


def pre_on_post_save(sender, **kwargs):
    post = kwargs['instance']
    if post.photo:
        max_width=300
        if post.photo.width > max_width or post.photo.height > max_width:
            processed_file = thumbnail(post.photo.file, max_width, max_width)
            post.photo.save(post.photo.name, File(processed_file))

pre_save.connect(pre_on_post_save, sender=Post)






