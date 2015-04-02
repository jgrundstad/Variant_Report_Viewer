from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from viewer import views

urlpatterns = patterns(
      '', 
      url(r'^$', views.index, name='index'),
      url(r'^new_bionimbus_id/$', views.new_bionimbus_id, name='new_bionimbus_id'),
      url(r'^new_sample/$', views.new_sample, name='new_sample'),
      url(r'^new_case/$', views.new_case, name='new_case'),
      url(r'^upload_vcf/$', views.upload_vcf, name='upload_vcf'),
      url(r'^files/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
