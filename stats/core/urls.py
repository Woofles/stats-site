from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^query/$', 'core.views.query', name='query'),
)