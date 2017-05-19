from django.conf.urls import include, url, patterns
from django.contrib import admin
from SAMain import views

urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^$', views.home, name='SA_home'))

urlpatterns += patterns('django.contrib.auth.views',
                        url(r'^login/$', 'login', {'template_name' : 'SAMain\login.html'}, name='SA_login'),
                        url(r'^logout/$', 'logout', {'next_page' : 'SA_home'}, name='SA_logout')),
