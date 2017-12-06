from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.index, name="generator"),
    url('^api/$', views.api, name="generator"),
]
