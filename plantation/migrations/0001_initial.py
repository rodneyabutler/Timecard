# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plantation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('county', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('longitude', models.CharField(max_length=128)),
                ('latitude', models.CharField(max_length=128)),
                ('information', models.TextField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
