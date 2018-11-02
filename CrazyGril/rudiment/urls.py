from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'rudiment.views.rudiment', name='rudiment'),
    url(r'content$', 'rudiment.views.content', name='content'),
    url(r'update_time_line$', 'rudiment.views.update_time_line', name='update_time_line'),
    url(r'project_log$', 'rudiment.views.project_log', name='project_log$'),
    url(r'^feedback', 'rudiment.views.feedback', name='feedback'),
    url(r'^list_feedback', 'rudiment.views.list_feedback', name='list_feedback'),
    url(r'^submit_feedback', 'rudiment.views.feedback_submit', name='submit_feedback'),
    # url(r'^Elk_Create', 'rudiment.views.Elk_Create', name='Elk_Create'),

   )

