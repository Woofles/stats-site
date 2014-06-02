from django.conf.urls import patterns, include, url

from django.contrib import admin
import core

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'core.views.index', name='index'),
    url(r'^core/, ', include('core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
