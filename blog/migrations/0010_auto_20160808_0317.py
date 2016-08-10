# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 03:17
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160806_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='jjal',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=blog.validators.get_file_path),
        ),
        migrations.AlterField(
            model_name='postcode',
            name='post_code',
            field=blog.fields.PostCodeField(max_length=10, validators=[blog.validators.post_code_validator, blog.validators.post_code_validator, blog.validators.post_code_validator]),
        ),
    ]