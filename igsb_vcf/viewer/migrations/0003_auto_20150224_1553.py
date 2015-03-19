# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_auto_20150224_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vcf',
            name='sample',
        ),
        migrations.AddField(
            model_name='vcf',
            name='bnid',
            field=models.ManyToManyField(to='viewer.Bnid'),
            preserve_default=True,
        ),
    ]
