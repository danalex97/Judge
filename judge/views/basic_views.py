from django.template.loader import get_template
from django.template import Context

from django.db.models import Q
from django.shortcuts import render_to_response
from judge.database.models import Question
from judge.database.models import Hack
from judge.database.models import Article

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def display_home(request):
	t = get_template('basic.html')
	html = t.render(Context({ 'path':'home' }))
	return HttpResponse(html)

def display_freshers(request):
	t = get_template('freshers.html')
	html = t.render(Context({ 'path':'freshers' }))
	return HttpResponse(html)

def no_page(req):
	html = "<html><body>No page<body><html>"
	return HttpResponse(html)

def render_qset(query):
	if query:
		qset = (
			Q(user__icontains=query) |
			Q(title__icontains=query) |
			Q(labels__icontains=query)
		)
	return qset

def render_my_response(my_file, res, aRes, qry, my_path):
	if aRes:
		return render_to_response(my_file, {
			"results": aRes,
			"path": my_path})
	else:
		return render_to_response(my_file, {
			"results":res,
			"query": qry,
			"path": my_path})

def display_by_class(request, input_class, template, name):
	query = request.GET.get('q', '')
	all_results = 0
	results = 0
	if query:
		qset = render_qset(query)
		results = input_class.objects.filter(qset).distinct()
	else:
		results = []
		all_results = input_class.objects.distinct()
	return render_my_response(template
		, results
		, all_results
		, query
		, name)

def display_questions(request):
	return display_by_class(request
		, Question
		, 'questions.html'
		, 'questions')

def display_tasks(request):
	pass

def display_hacks(request):
	return display_by_class(request
		, Hack
		, 'hacks.html'
		, 'hack')

def display_articles(request):
	return display_by_class(request
		, Article
		, 'articles.html'
		, 'articles')
