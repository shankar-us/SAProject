from django.conf.urls import include, url
from django.contrib import admin
from SAMain import views


urlpatterns = {
    # Examples:
    # url(r'^$', 'SAProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home)
}
