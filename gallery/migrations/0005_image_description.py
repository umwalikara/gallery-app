# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_remove_image_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
