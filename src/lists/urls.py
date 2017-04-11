from django.conf.urls import url, include 
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from lists import views 


urlpatterns = [
    url(r'^users', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

