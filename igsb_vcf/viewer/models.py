from django.db import models
import datetime

class Case(models.Model):
  name = models.CharField(max_length=64, verbose_name="Case Name")
  def __str__(self):
    return self.name


class Caller(models.Model):
  name = models.CharField(max_length=64, verbose_name="Caller Name")
  def __str__(self):
    return self.name


class Sample(models.Model):
  name = models.CharField(max_length=48, verbose_name='Sample Name')
  case = models.ForeignKey(Case)
  def __str__(self):
    return "%s - %s" % (str(self.case), str(self.name))


class Vcf(models.Model):
  caller = models.ForeignKey(Caller)
  case = models.ForeignKey(Case)
  upload_date = models.DateTimeField('Date Uploaded', auto_now=True)
  sample = models.ManyToManyField(Sample)
  vcf_file = models.FileField('Vcf File', upload_to='')
  #report_file = models.FileField('Report File', upload_to='', blank=True)
  def __str__(self):
    return str(self.upload_date)


class Bnid(models.Model):
  bnid = models.CharField(max_length=12, verbose_name='Bionimbus ID')
  sample = models.ForeignKey(Sample, related_name="bnid_sample")
  def __str__(self):
    return self.bnid

