# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bnid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bnid', models.CharField(max_length=12, verbose_name=b'Bionimbus ID')),
                ('description', models.CharField(max_length=256, verbose_name=b'Description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Caller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'Caller Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now=True, verbose_name=b'Date Uploaded')),
                ('report_file', models.FileField(upload_to=b'', verbose_name=b'Report File')),
                ('bnids', models.ManyToManyField(to='viewer.Bnid', verbose_name=b'Bionimbus ID')),
                ('caller', models.ForeignKey(to='viewer.Caller')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=48, verbose_name=b'Sample Name')),
                ('description', models.CharField(max_length=256, verbose_name=b'Sample Description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'Study Name')),
                ('description', models.CharField(max_length=256, verbose_name=b'Study Description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sample',
            name='study',
            field=models.ForeignKey(to='viewer.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='study',
            field=models.ForeignKey(to='viewer.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bnid',
            name='sample',
            field=models.ForeignKey(to='viewer.Sample'),
            preserve_default=True,
        ),
    ]
