# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bnid',
            name='description',
            field=models.CharField(max_length=256, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
    ]
