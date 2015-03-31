from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from viewer import views

urlpatterns = patterns(
      '', 
      url(r'^$', views.index, name='index'),
      url(r'^bionimbus_ids/$', views.bionimbus_ids, name='bionimbus_ids'),
      url(r'^upload_vcf/$', views.upload_vcf, name='upload_vcf'),
      url(r'^files/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
      url(r'^new_case/$', views.new_case, name='new_case')
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
