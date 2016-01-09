from django.conf.urls import patterns, include, url

from django.contrib import admin
from judge.views.date_views import date_time, hours_ahead

from judge.views.basic_views import display_home
from judge.views.basic_views import display_questions
from judge.views.basic_views import no_page

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^time/$', date_time),
    url(r'^time/plus/(\d+)/$', hours_ahead),
    
    url(r'^home/$', display_home),
    url(r'^$', display_home),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^questions/$', display_questions),
    
    url(r'.+', no_page),
)
