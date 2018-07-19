# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 13:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=140)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime(2018, 7, 18, 13, 4, 4, 855310))),
            ],
        ),
    ]
