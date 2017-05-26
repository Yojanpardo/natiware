# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('rol', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
