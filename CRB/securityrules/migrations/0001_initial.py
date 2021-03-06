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
            name='SecurityRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision', models.CharField(choices=[(b'log', b'Log Request'), (b'accept', b'Accept Request'), (b'deny', b'Deny Request'), (b'redirect', b'Redirect Request to captive Portal'), (b'blockall', b'* Block any Request, (not recommended)')], max_length=250)),
                ('source_IP', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
