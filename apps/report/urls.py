from django.conf.urls import patterns, url
from .views import index2, ReportSave

urlpatterns = patterns('',
	url(r'^$', 'apps.report.views.index', name='index'),
	url(r'^index2/$', index2.as_view(), name='index2'),
	url(r'^save/$', ReportSave.as_view(), name='save'),
	)
