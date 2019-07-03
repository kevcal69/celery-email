# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_address', models.EmailField(max_length=254)),
                ('to_address', models.CharField(max_length=1024)),
                ('subject', models.CharField(blank=True, max_length=256, null=True)),
                ('body', models.TextField()),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Sent'), (2, 'Failed')], default=0)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('when_sent', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['when'],
            },
        ),
    ]