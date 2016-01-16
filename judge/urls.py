from django.conf.urls import patterns, include, url

from django.contrib import admin
from judge.views.date_views import date_time, hours_ahead

from judge.views.basic_views import display_home
from judge.views.basic_views import display_questions
from judge.views.basic_views import display_articles
from judge.views.basic_views import display_tasks
from judge.views.basic_views import display_freshers
from judge.views.basic_views import display_hacks
from judge.views.basic_views import no_page

from judge.views.cookie_views import login
from judge.views.cookie_views import auth_view
from judge.views.cookie_views import logout
from judge.views.cookie_views import loggedin
from judge.views.cookie_views import invalid_login

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^time/$', date_time),
    url(r'^time/plus/(\d+)/$', hours_ahead),
    
    url(r'^home/$', display_home),
    url(r'^$', display_home),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^questions/$', display_questions),
    url(r'^tasks/$', display_tasks),
    url(r'^hacks/$', display_hacks),
    url(r'^articles/$', display_articles),
    url(r'^freshers/$', display_freshers),
    
    url(r'^accounts/login/$', login),
    url(r'^accounts/auth/$', auth_view),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/loggedin/$', loggedin),
    url(r'^accounts/invalid/$', invalid_login),
    
    url(r'.+', no_page),
) 
