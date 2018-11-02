from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^test', 'task.views.tasks', name='test'),
    url(r'^bb', 'task.views.testmk', name='test1'),
    url(r'^shell_add', 'task.views.shell_add', name='shell_add'),
    url(r'^ajax_get_range', 'task.views.ajax_get_range', name='ajax_get_range'),
    url(r'^shell_exe', 'task.views.shell_exe', name='shell_exe'),
    url(r'^because_accres', 'task.views.because_accres', name='because_accres'),
    url(r'^show_tasks', 'task.views.show_tasks', name='show_tasks'),
    url(r'^ajax_show_tasks', 'task.views.ajax_show_tasks', name='ajax_show_tasks'),
    url(r'^ajax_upload', 'task.views.ajax_upload', name='ajax_upload'),
    url(r'^upf', 'task.views.upf', name='upf'),
    url(r'^tun_upf', 'task.views.tun_upf', name='tun_upf'),
    url(r'^ansible_show', 'task.views.ansible_show', name='ansible_show'),


   )
