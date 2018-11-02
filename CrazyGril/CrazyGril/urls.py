from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'CrazyGril.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('rudiment.urls', namespace='rudiment')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^cmdb/', include('cmdb.urls', namespace='cmdb')),
    url(r'^docker/', include('docker.urls', namespace='docker')),
    url(r'^conf/', include('conf.urls', namespace='conf')),
    url(r'^charts/', include('charts.urls', namespace='charts')),
    url(r'^task/', include('task.urls', namespace='task')),
]
