# Generated by Django 2.2.4 on 2020-08-08 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0070_auto_20200808_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grant',
            name='grant_type_purge',
        ),
    ]