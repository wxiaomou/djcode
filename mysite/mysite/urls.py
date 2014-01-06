from django.conf.urls import patterns, include, url
from mysite.views import index, hello, current_datetime, hours_ahead

urlpatterns = patterns('',
		url(r'^$', index),
		url(r'^hello/$', hello),
		url(r'^time/$', current_datetime),
		url(r'^time/plus/(\d{1,2})$', hours_ahead),
)
