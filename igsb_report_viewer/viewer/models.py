from django.db import models


class Study(models.Model):
    name = models.CharField(max_length=64, verbose_name="Study Name")
    description = models.CharField(max_length=256,
                                   verbose_name="Study Description",
                                   blank=True)
    creation_date = models.DateTimeField('Date Created', auto_now=True,
                                         blank=True)

    def __str__(self):
        return self.name


class Caller(models.Model):
    name = models.CharField(max_length=64, verbose_name="Caller Name")

    def __str__(self):
        return self.name


class Sample(models.Model):
    name = models.CharField(max_length=48, verbose_name='Sample Name')
    description = models.CharField(max_length=256,
                                   verbose_name="Sample Description",
                                   blank=True)
    study = models.ForeignKey(Study)
    creation_date = models.DateTimeField('Date Created', auto_now=True,
                                         blank=True)

    def __str__(self):
        return str(self.name)


class Bnid(models.Model):
    sample = models.ForeignKey(Sample)
    bnid = models.CharField(max_length=12, verbose_name='Bionimbus ID')
    description = models.CharField(max_length=256, verbose_name='Description',
                                   blank=True)
    creation_date = models.DateTimeField('Date Created', auto_now=True,
                                         blank=True)

    def __str__(self):
        return '{} ({})'.format(str(self.sample), str(self.bnid))


class Report(models.Model):
    caller = models.ForeignKey(Caller)
    study = models.ForeignKey(Study)
    upload_date = models.DateTimeField('Date Uploaded', auto_now=True)
    bnids = models.ManyToManyField(Bnid, verbose_name='Bionimbus ID')
    report_file = models.FileField('Report File', upload_to='')

    def __str__(self):
        return str(self.upload_date)