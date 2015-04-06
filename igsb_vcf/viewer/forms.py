from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from models import Bnid, Sample, Caller, Vcf, Case


class BnidForm(forms.ModelForm):
  class Meta:
    model = Bnid
    fields = ['sample', 'bnid']


class SampleForm(forms.ModelForm):
  class Meta:
    model = Sample
    fields = ['case', 'name']


class CallerForm(forms.ModelForm):
  class Meta:
    model = Caller


class VcfForm(forms.ModelForm):
  vcf_file = forms.FileField(widget=AdminFileWidget)
  class Meta:
    model = Vcf
    fields = ['case', 'sample', 'caller', 'vcf_file']


class CaseForm(forms.ModelForm):
  class Meta:
    model = Case

