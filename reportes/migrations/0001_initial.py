# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AGAFF',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('log', models.CharField(max_length=80)),
                ('ambiente', models.CharField(max_length=20)),
                ('error', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(verbose_name='fecha error')),
                ('detalle', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='COB',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('log', models.CharField(max_length=70)),
                ('ambiente', models.CharField(max_length=20)),
                ('error', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(verbose_name='fecha error')),
                ('detalle', models.CharField(max_length=10000)),
            ],
        ),
    ]
