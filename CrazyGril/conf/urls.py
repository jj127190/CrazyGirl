from django.conf.urls import patterns, url

urlpatterns = patterns('',
   url(r'^conf_show', 'conf.views.conf_show', name='conf_show'),
   url(r'^conf_save', 'conf.views.conf_save', name='conf_save'),

)