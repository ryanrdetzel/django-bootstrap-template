from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'django_bootstrap.views.home', name='home'),
    # url(r'^django_bootstrap/', include('django_bootstrap.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
