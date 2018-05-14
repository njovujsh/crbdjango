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
            name='LegacyTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_engine', models.CharField(choices=[(b'mysql', b'MYSQL Database Engine'), (b'postgres', b'Postgre Database Engine'), (b'sqlite3', b'Sqlite3 Database Engine(Requires developer integration)')], max_length=250)),
                ('database_hostname', models.CharField(max_length=250)),
                ('database_port', models.CharField(max_length=250)),
                ('database_username', models.CharField(max_length=250)),
                ('database_password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ReplicationDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_engine', models.CharField(choices=[(b'mysql', b'MYSQL Database Engine'), (b'postgres', b'Postgre Database Engine')], max_length=250)),
                ('destination_hostname', models.CharField(max_length=250)),
                ('destination_port', models.CharField(max_length=250)),
                ('destination_username', models.CharField(max_length=250)),
                ('destination_password', models.CharField(max_length=250)),
            ],
        ),
    ]
