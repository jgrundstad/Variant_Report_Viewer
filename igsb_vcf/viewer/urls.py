from django.conf.urls import patterns, url
from viewer import views

urlpatterns = patterns(
    '', 
    url(r'^$', views.index, name='index'),
    url(r'^bionimbus_ids/$', views.bionimbus_ids, name='bionimbus_ids'),
    )
