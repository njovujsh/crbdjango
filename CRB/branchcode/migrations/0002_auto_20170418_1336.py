# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchcode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requiredheader',
            name='creation_date',
            field=models.CharField(default=b'2017-04-18', max_length=100),
        ),
    ]
