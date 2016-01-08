from django.conf.urls import patterns, include, url

from django.contrib import admin
from judge.views.date_views import date_time, hours_ahead, no_page
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^time/$', date_time),
    url(r'^time/plus/(\d+)/$', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    url('.+', no_page),
)
