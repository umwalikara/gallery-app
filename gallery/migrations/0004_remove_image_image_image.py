# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_image',
        ),
    ]
