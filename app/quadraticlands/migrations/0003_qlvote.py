# Generated by Django 2.2.4 on 2021-04-25 16:28

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0172_auto_20210216_0820'),
        ('quadraticlands', '0002_gtcsteward'),
    ]

    operations = [
        migrations.CreateModel(
            name='QLVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(default='', max_length=255)),
                ('vote', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('full_msg', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_status', to='dashboard.Profile')),
            ],
        ),
    ]