# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ValidatedAndSaved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('filename', models.FileField(blank=True, max_length=500, null=True, upload_to=b'.')),
                ('imagename', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
