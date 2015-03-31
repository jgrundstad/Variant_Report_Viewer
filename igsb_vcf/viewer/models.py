from django.db import models

class Case(models.Model):
  name = models.CharField(max_length=64, verbose_name="Case Name")
  def __str__(self):
    return self.name


class Caller(models.Model):
  name = models.CharField(max_length=64, verbose_name="Caller Name")
  def __str__(self):
    return self.name


class Vcf(models.Model):
  caller = models.ForeignKey(Caller)
  case = models.ForeignKey(Case)
  vcf_file = models.FileField(upload_to='')
  def __str__(self):
    return self.caller.name


class Sample(models.Model):
  name = models.CharField(max_length=48, verbose_name='Sample Name')
  case = models.ForeignKey(Case)
  vcf = models.ForeignKey(Vcf, blank=True)
  def __str__(self):
    return self.name


class Bnid(models.Model):
  bnid = models.CharField(max_length=12, verbose_name='Bionimbus ID')
  sample = models.ForeignKey(Sample)
  def __str__(self):
    return self.bnid

