# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-01 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=30)),
                ('actor_movie', models.CharField(max_length=50)),
                ('gener', models.CharField(max_length=50)),
            ],
        ),
    ]