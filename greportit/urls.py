from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #'apps',
    #url(r'^$', 'report.views.index', name='home'),
    #url(r'^report/save$', 'report.views.report_save', name='report_save'),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^init/', include('apps.init.urls')),

    url(r'^report/', include('apps.report.urls')),

    # url(r'^greportit/', include('greportit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(?P.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),
    url(r'^ajax-upload/', include('ajax_upload.urls')),
)
