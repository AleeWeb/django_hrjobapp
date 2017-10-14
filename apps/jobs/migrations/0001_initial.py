# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_descp', models.CharField(max_length=500)),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
