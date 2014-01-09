from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def index(request):
	return HttpResponse("Index")

def hello(request):
	return HttpResponse("Hello Word!")

def current_datetime(request):
	now = datetime.datetime.now()
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date': now}))
	#return HttpResponse(html)
	return render(request, 'current_datetime.html', {'current_date': now, 'offset': 2 })

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
#	assert False 
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>It is now %s offset %s. </body></html>" % (now, offset)
	return HttpResponse(html)
