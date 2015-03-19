from django.contrib import admin
from viewer.models import Project, Tissue, Platform, Bnid, Sample
from viewer.models import Case, Caller, Vcf


class ProjectAdmin(admin.ModelAdmin):
  fields = ['name']

class SampleAdmin(admin.ModelAdmin):
  model = Sample

class TissueAdmin(admin.ModelAdmin):
  model = Tissue

class PlatformAdmin(admin.ModelAdmin):
  model = Platform

class BnidAdmin(admin.ModelAdmin):
  list_display = ('bnid', 'tissue', 'platform')

class CaseAdmin(admin.ModelAdmin):
  model = Case
  filter_horizontal = ('sample',)

class CallerAdmin(admin.ModelAdmin):
  display = ['name']

class VcfAdmin(admin.ModelAdmin):
  model = Vcf
  filter_horizontal = ('bnid',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Tissue, TissueAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Bnid, BnidAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Caller, CallerAdmin)
admin.site.register(Vcf, VcfAdmin)
