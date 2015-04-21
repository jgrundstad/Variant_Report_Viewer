from django.contrib import admin
from models import Bnid, Sample
from models import Study, Caller, Vcf


class BnidAdmin(admin.ModelAdmin):
    model = Bnid


class SampleAdmin(admin.ModelAdmin):
    model = Sample


class CallerAdmin(admin.ModelAdmin):
    display = ['name']


class VcfAdmin(admin.ModelAdmin):
    model = Vcf
    list_display = ('caller', 'vcf_file', )


class StudyAdmin(admin.ModelAdmin):
    model = Study
    list_display = ('name', 'description')


admin.site.register(Sample, SampleAdmin)
admin.site.register(Bnid, BnidAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Caller, CallerAdmin)
admin.site.register(Vcf, VcfAdmin)
