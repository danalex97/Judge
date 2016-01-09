from django.template.loader import get_template
from django.template import Context

from django.db.models import Q
from django.shortcuts import render_to_response
from judge.database.models import Question

from django.http import HttpResponse

def display_home(request):
	t = get_template('basic.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def no_page(req):
	html = "<html><body>No page<body><html>"
	return HttpResponse(html)

def display_questions(request):
	query = request.GET.get('q', '')
	all_results = 0
	if query:
		qset = (
			Q(user__icontains=query) |
			Q(title__icontains=query) |
			Q(content__icontains=query)
		)
		results = Question.objects.filter(qset).distinct()
	else:
		results = []
		all_results = Question.objects.distinct()
	if all_results:
		return render_to_response('questions.html', {
			"results": all_results,
		})
	else:
		return render_to_response('questions.html', {
			"results": results,
			"query": query
		})
