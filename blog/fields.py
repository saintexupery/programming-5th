import re
from django.db import models
from django.forms import ValidationError
from .validators import phone_number_validator, post_code_validator


class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(phone_number_validator)
        super().__init__(*args, **kwargs)


class PostCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(post_code_validator)
        super().__init__(*args, **kwargs)