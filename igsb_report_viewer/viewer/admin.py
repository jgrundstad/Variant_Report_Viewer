from django.contrib import admin
from models import Bnid, Sample, Study, Caller, Report



class BnidAdmin(admin.ModelAdmin):
    model = Bnid


class SampleAdmin(admin.ModelAdmin):
    model = Sample


class CallerAdmin(admin.ModelAdmin):
    display = ['name']


class ReportAdmin(admin.ModelAdmin):
    model = Report
    list_display = ('caller', 'report_file', 'upload_date')


class StudyAdmin(admin.ModelAdmin):
    model = Study
    list_display = ('name', 'description')


admin.site.register(Sample, SampleAdmin)
admin.site.register(Bnid, BnidAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Caller, CallerAdmin)
admin.site.register(Report, ReportAdmin)
