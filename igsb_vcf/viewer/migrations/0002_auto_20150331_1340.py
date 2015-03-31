# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='vcf',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='bnid',
        ),
        migrations.RemoveField(
            model_name='vcf',
            name='sample',
        ),
        migrations.AddField(
            model_name='bnid',
            name='sample',
            field=models.ForeignKey(default=1, to='viewer.Sample'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='case',
            field=models.ForeignKey(default=1, to='viewer.Case'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='vcf',
            field=models.ForeignKey(default=1, blank=True, to='viewer.Vcf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcf',
            name='case',
            field=models.ForeignKey(default=1, to='viewer.Case'),
            preserve_default=False,
        ),
    ]
