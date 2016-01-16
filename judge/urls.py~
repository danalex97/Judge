from django.conf.urls import patterns, include, url

from django.contrib import admin
from judge.views.date_views import date_time, hours_ahead

from judge.views.basic_views import display_home
from judge.views.basic_views import display_questions
from judge.views.basic_views import display_articles
from judge.views.basic_views import display_tasks
from judge.views.basic_views import display_hacks
from judge.views.basic_views import no_page

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
    
    url(r'.+', no_page),
) 
