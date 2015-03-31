# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_auto_20150331_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnid',
            name='bnid',
            field=models.CharField(max_length=12, verbose_name=b'Bionimbus ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='caller',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Caller Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='case',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Case Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='name',
            field=models.CharField(max_length=48, verbose_name=b'Sample Name'),
            preserve_default=True,
        ),
    ]
