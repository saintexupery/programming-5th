from django.conf import settings
from django.core.files import File
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.db import models
from django.utils import timezone
from .validators import lnglat_validator, MinLengthValidator, phone_number_validator, ZipCodeValidator, get_file_path
from .fields import PhoneNumberField, PostCodeField
from .utils import square_image, thumbnail


class Post(models.Model):
    author = models.CharField(max_length=50) # ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100,
        validators=[MinLengthValidator(4)],
        verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.',
        validators=[MinLengthValidator(10)])
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)
    photo = models.ImageField(upload_to=get_file_path, blank=True, null=True) # blank 값이 비어있는 것에 대한 유효성 검사
    # null은 지정할 일이 거의 없다. null은 python에서 None값. null이 의미 있는 경우에는 ForeignKey에만 있다.

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])
        #'blog.views.post_detail'이 작동하지 않는 이유는 url의 두 번째 인자가 문자열이 아닌 함수이기 때문이다.


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    jjal = models.ImageField(blank=True)
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
    if post.photo: # 사진이 저장된 경로가 존재한다면
        # post.photo : 이미지 저장 경로
        # post.photo.name : 이미지 파일명
        # post.photo.path : 이미지 저장 absolute url
        # post.photo.url : 이미지 url
        # post.photo.file : 경로에 있는 파일에 대하여 읽고, 쓸 수 있는 기능을 제공
        # post.photo.with (ImageField only)
        # post.photo.height (ImageField only)
        max_width=300
        if post.photo.width > max_width or post.photo.height > max_width:
            processed_file = thumbnail(post.photo.file, max_width, max_width)
            post.photo.save(post.photo.name, File(processed_file))

pre_save.connect(pre_on_post_save, sender=Post) # Post모델이 호출되고 저장하기 직전에 on_pre_save라는 함수를 호출하겠다.






