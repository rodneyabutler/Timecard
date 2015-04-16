# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantation', '0002_auto_20150413_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='counties',
            options={'verbose_name_plural': 'counties'},
        ),
    ]
