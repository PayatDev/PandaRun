# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20171122_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='full_runner',
            name='shirt_size',
            field=models.CharField(choices=[('3S', '3S ขนาดรอบอก 32 นิ้ว'), ('2S', '2S ขนาดรอบอก 34 นิ้ว'), ('S', 'S ขนาดรอบอก 36 นิ้ว'), ('M', 'M ขนาดรอบอก 38 นิ้ว'), ('L', 'L ขนาดรอบอก 40 นิ้ว'), ('XL', 'XL ขนาดรอบอก 42 นิ้ว'), ('2XL', '2XL ขนาดรอบอก 44 นิ้ว'), ('3XL', '3XL ขนาดรอบอก 46 นิ้ว'), ('4XL', '4XL ขนาดรอบอก 48 นิ้ว')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='half_runner',
            name='shirt_size',
            field=models.CharField(choices=[('3S', '3S ขนาดรอบอก 32 นิ้ว'), ('2S', '2S ขนาดรอบอก 34 นิ้ว'), ('S', 'S ขนาดรอบอก 36 นิ้ว'), ('M', 'M ขนาดรอบอก 38 นิ้ว'), ('L', 'L ขนาดรอบอก 40 นิ้ว'), ('XL', 'XL ขนาดรอบอก 42 นิ้ว'), ('2XL', '2XL ขนาดรอบอก 44 นิ้ว'), ('3XL', '3XL ขนาดรอบอก 46 นิ้ว'), ('4XL', '4XL ขนาดรอบอก 48 นิ้ว')], default=None, max_length=2),
        ),
    ]
