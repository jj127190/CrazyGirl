from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'get_asset_info', 'api.views.get_asset_info', name='get_asset_info'),
    url(r'get_sysInfo', 'api.views.get_sysInfo', name='get_sysInfo'),
    url(r'^get_dockerInfo', 'api.views.get_dockerInfo', name='get_dockerInfo'),
    url(r'^test', 'api.views.test', name='test'),
    url(r'^auto_git', 'api.views.auto_git', name='auto_git'),
    url(r'^get_dockerStats', 'api.views.get_dockerStats', name='get_dockerStats'),
    url(r'^auto_git2', 'api.views.auto_git2', name='auto_git2'),
   )
