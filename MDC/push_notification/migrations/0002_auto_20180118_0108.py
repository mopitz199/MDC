# Generated by Django 2.0.1 on 2018-01-18 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('push_notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pushnotificationtoken',
            old_name='result',
            new_name='key',
        ),
    ]
