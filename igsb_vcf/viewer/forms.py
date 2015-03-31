from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from models import Bnid, Sample, Caller, Vcf, Case


class BnidForm(forms.ModelForm):
  class Meta:
    model = Bnid


class SampleForm(forms.ModelForm):
  class Meta:
    model = Sample


class CallerForm(forms.ModelForm):
  class Meta:
    model = Caller


class VcfForm(forms.ModelForm):
  vcf_file = forms.FileField(widget=AdminFileWidget)
  class Meta:
    model = Vcf


class CaseForm(forms.ModelForm):
  class Meta:
    model = Case

