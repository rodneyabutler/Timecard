# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plantation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('county_name', models.CharField(max_length=128)),
                ('county_information', models.TextField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_lat', models.CharField(max_length=120)),
                ('current_long', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('end_lat', models.CharField(max_length=120)),
                ('end_long', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='plantation',
            name='webpage',
            field=models.URLField(default=datetime.datetime(2015, 4, 14, 0, 31, 28, 658000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
