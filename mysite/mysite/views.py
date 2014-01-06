from django.http import HttpResponse, Http404
import datetime

def index(request):
	return HttpResponse("Index")

def hello(request):
	return HttpResponse("Hello Word!")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s. </body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
#	assert False 
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>It is now %s offset %s. </body></html>" % (now, offset)
	return HttpResponse(html)
