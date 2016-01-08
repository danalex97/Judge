from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse
import datetime

def date_time(request):
	now = datetime.datetime.now()
	t = get_template('datetime.html')
	html = t.render(Context({'datetime': now , 'plus' : 0}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	offset = int(offset)
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	t = get_template('datetime.html') 
	html = t.render(Context({'datetime': now, 'plus': offset}))
	return HttpResponse(html)

def no_page(req):
	html = "<html><body>No page<body><html>"
	return HttpResponse(html)
