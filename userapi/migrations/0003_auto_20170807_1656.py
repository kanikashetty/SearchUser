# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-07 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0002_auto_20170807_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
