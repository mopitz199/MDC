# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0006_trade_ts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tradePics'),
        ),
    ]
