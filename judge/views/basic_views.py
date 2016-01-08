from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse

def display_home(request):
	t = get_template('basic.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def no_page(req):
	html = "<html><body>No page<body><html>"
	return HttpResponse(html)
