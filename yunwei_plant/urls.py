from django.conf.urls import patterns, include, url
from web.views import Login
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yunwei_plant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/',include('web.urls')),
    url(r'^$', Login),
)
