from django.contrib import admin
from viewer.models import Bnid, Sample
from viewer.models import Case, Caller, Vcf


class BnidAdmin(admin.ModelAdmin):
  model = Bnid


class SampleAdmin(admin.ModelAdmin):
  model = Sample


class CallerAdmin(admin.ModelAdmin):
  display = ['name']


class VcfAdmin(admin.ModelAdmin):
  model = Vcf
  list_display = ('caller', 'vcf_file',)


class CaseAdmin(admin.ModelAdmin):
  model = Case


admin.site.register(Sample, SampleAdmin)
admin.site.register(Bnid, BnidAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Caller, CallerAdmin)
admin.site.register(Vcf, VcfAdmin)
