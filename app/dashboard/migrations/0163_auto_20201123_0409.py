# Generated by Django 2.2.4 on 2020-11-23 04:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0162_auto_20201112_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_ens_verified',
            field=models.BooleanField(default=False),
        ),
    ]