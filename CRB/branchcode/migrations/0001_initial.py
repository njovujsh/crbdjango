# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_Code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BranchNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_Code', models.CharField(blank=True, max_length=30)),
                ('Branch_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('votecode', models.CharField(blank=True, max_length=255, null=True)),
                ('coordinate', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PIIdentificationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi_identification_code', models.CharField(max_length=120, unique=True)),
                ('insitution_Name', models.CharField(max_length=120)),
                ('date', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RequiredHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default=b'H', max_length=100)),
                ('branch_code', models.CharField(blank=True, default=b'', max_length=100, unique=True)),
                ('submission_date', models.CharField(default=b'', max_length=100)),
                ('version_number', models.CharField(blank=True, default=b'', max_length=100)),
                ('creation_date', models.CharField(default=b'2016-01-04', max_length=100)),
                ('branch_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='branchcode.BranchNames')),
                ('pi_identification_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branchcode.PIIdentificationCode')),
            ],
        ),
        migrations.CreateModel(
            name='Subcounties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branchcode.Districts')),
            ],
        ),
        migrations.AddField(
            model_name='parishes',
            name='subcounty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branchcode.Subcounties'),
        ),
        migrations.AddField(
            model_name='districts',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branchcode.Regions'),
        ),
    ]
