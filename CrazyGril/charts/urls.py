from django.conf.urls import patterns, url

urlpatterns = patterns('',
   url(r'^info_shows', 'charts.views.info_shows', name='info_shows'),
   url(r'^info_show', 'charts.views.info_show', name='info_show'),
   url(r'^info_test', 'charts.views.info_test', name='info_test'),
   url(r'^get_disk', 'charts.views.get_disk', name='get_disk'),
   url(r'^get_cpu', 'charts.views.get_cpu', name='get_cpu'),
   url(r'^get_eth', 'charts.views.get_eth', name='get_eth'),
  url(r'^info_type_mem', 'charts.views.info_type_mem', name='info_type_mem'),
  url(r'^info_type_disk', 'charts.views.info_type_disk', name='info_type_disk'),
  url(r'^info_type_cpu', 'charts.views.info_type_cpu', name='info_type_cpu'),
  url(r'^info_type_eth', 'charts.views.info_type_eth', name='info_type_eth'),
url(r'^mongo_typeinfos', 'charts.views.mongo_typeinfos', name='mongo_typeinfos'),


)
