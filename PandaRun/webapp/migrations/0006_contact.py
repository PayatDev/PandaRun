# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20171122_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('mobile', models.CharField(default=None, max_length=10)),
                ('comment', models.TextField(default=None, max_length=500)),
            ],
        ),
    ]
