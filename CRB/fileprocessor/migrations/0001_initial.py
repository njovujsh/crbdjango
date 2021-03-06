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
            name='FileUploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('uploaded_name', models.FileField(upload_to=b'.')),
                ('uploaded_by', models.CharField(max_length=100)),
                ('content_type', models.CharField(blank=True, max_length=100, null=True)),
                ('file_size', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
