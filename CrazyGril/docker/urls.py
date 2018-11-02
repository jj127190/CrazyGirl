from django.conf.urls import patterns, url

urlpatterns = patterns('',
   url(r'^image_build', 'docker.views.image_build', name='image_build'),
   url(r'^build_add', 'docker.views.build_add', name='build_add'),
   url(r'^image_create_add', 'docker.views.image_create_add', name='image_create_add'),
   url(r'^image_delete', 'docker.views.image_delete', name='image_delete'),
   url(r'^image_edit', 'docker.views.image_edit', name='image_edit'),
   url(r'^upload_dockerfile', 'docker.views.upload_dockerfile', name='upload_dockerfile'),
   url(r'^search_build_image', 'docker.views.search_build_image', name='search_build_image'),
   url(r'^update_images', 'docker.views.update_images', name='update_images'),
   url(r'^show_con', 'docker.views.show_con', name='show_con'),
   url(r'^container_show', 'docker.views.container_show', name='container_show'),
   url(r'^show_stats', 'docker.views.show_stats', name='show_stats'),
   url(r'^ajax_docker_stats', 'docker.views.ajax_docker_stats', name='ajax_docker_stats'),
   url(r'^query_stat', 'docker.views.query_stat', name='query_stat'),
   url(r'^ajax_query_stats/(?P<hostip>\d+)/$', 'docker.views.ajax_query_stats', name='ajax_query_stats'),
   url(r'^docker_echarts', 'docker.views.docker_echarts', name='docker_echarts'),
   url(r'^Ajax_getInfo', 'docker.views.Ajax_getInfo', name='Ajax_getInfo'),
   url(r'^container_e', 'docker.views.container_e', name='container_e'),
   url(r'^Ajax_tt', 'docker.views.Ajax_tt', name='Ajax_tt'),
   url(r'^t_get_conec', 'docker.views.t_get_conec', name='t_get_conec'),
   url(r'^search_c', 'docker.views.search_c', name='search_c'),




   # url(r'^query_stat/(?P<hostip>\d+)/$', 'docker.views.query_stat', name='query_stat'),
   # url(r'^Elk_Create', 'rudiment.views.Elk_Create', name='Elk_Create'),

   )

