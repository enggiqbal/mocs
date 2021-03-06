from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^maps/', include('maps.urls')),
    url(r'^nsf_maps/', include('nsf_maps.urls')),
    url(r'^dblp/', include('dblp.urls')),
    url(r'^nsf/', include('nsf.urls')),
    url(r'^reload/django$', 'views.reload_site'),
    url(r'^reload/celery$', 'views.restart_celery'),
    url(r'^reload/db$', 'views.syncdb'),
)
