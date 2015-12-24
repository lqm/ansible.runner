from django.conf.urls import patterns, include, url

from django.contrib import admin
from web.views import Login,index,machine_add,machine,machine_modify,motify_list,logout,ansible_hostsguanli,ansible_cmd,groupadd
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yunwei_plant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', Login),
    url(r'^login1/$', Login),
    url(r'^ansible_hosts/$',ansible_hostsguanli ),
    url(r'^ansible_cmd/$',ansible_cmd ),
    url(r'^index/$', index),
    url(r'^olmachine/$',machine ),
    url(r'^add/$',machine_add ),
    url(r'^modify/$',machine_modify ),
    # url(r'^del_machine/$',machine_del ),
    url(r'^list/(\d*)',motify_list ),
    url(r'^logout/$', logout),
    url(r'^groupadd/$', groupadd),

   
)
