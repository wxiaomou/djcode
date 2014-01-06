from django.conf.urls import patterns, include, url
from mysite.views import hello

urlpatterns = patterns('',
		    url(r'^hello/$', hello),
)
