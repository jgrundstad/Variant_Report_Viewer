from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^restricted/$', views.restricted, name='restricted'),
                       url(r'^permission/$', views.permission, name='permission'),
                       url(r'^new_bionimbus_id/$', views.new_bionimbus_id,
                           name='new_bionimbus_id'),
                       url(r'^new_sample/$', views.new_sample, name='new_sample'),
                       url(r'^new_study/$', views.new_study, name='new_study'),
                       url(r'^upload_vcf/$', views.upload_vcf, name='upload_vcf'),
                       url(r'^files/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)