from django.db import models


class Project(models.Model):
  name = models.CharField(max_length=48)

  def __str__(self):
    return self.name


class Tissue(models.Model):
  name = models.CharField(max_length=32)
  
  def __str__(self):
    return self.name


class Platform(models.Model):
  name = models.CharField(max_length=64)

  def __str__(self):
    return self.name


class Bnid(models.Model):
  bnid = models.CharField(max_length=12)
  tissue = models.ForeignKey(Tissue)
  platform = models.ForeignKey(Platform)

  def __str__(self):
    return self.bnid


class Sample(models.Model):
  name = models.CharField(max_length=48)
  project = models.ForeignKey(Project)
  bnid = models.ManyToManyField(Bnid)

  def __str__(self):
    return self.name


class Case(models.Model):
  name = models.CharField(max_length=64)
  sample = models.ManyToManyField(Sample)

  def __str__(self):
    return self.name


class Caller(models.Model):
  name = models.CharField(max_length=64)

  def __str__(self):
    return self.name


class Vcf(models.Model):
  bnid = models.ManyToManyField(Bnid)
  caller = models.ForeignKey(Caller)

  def __str__(self):
    return self.caller.name

