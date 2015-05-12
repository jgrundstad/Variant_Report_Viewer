# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bnid',
            name='creation_date',
            field=models.DateTimeField(default=datetime.date(2015, 5, 12), verbose_name=b'Date Created', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='creation_date',
            field=models.DateTimeField(default=datetime.date(2015, 5, 12), verbose_name=b'Date Created', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='creation_date',
            field=models.DateTimeField(default=datetime.date(2015, 5, 12), verbose_name=b'Date Created', auto_now=True),
            preserve_default=False,
        ),
    ]
