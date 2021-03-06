from django.template.loader import get_template
from django.template import Context, RequestContext

from django.db.models import Q
from django.shortcuts import render_to_response

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def login(request):
	c = {'path': 'accounts'}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	return render_to_response('acc.html', 
		{'full_name': request.user.username,
		 'path': 'accounts'} )

def invalid_login(request):
	return render_to_response('wrong.html',
		{'path': 'accounts'} )

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html', 
		{'path': 'accounts'} )
