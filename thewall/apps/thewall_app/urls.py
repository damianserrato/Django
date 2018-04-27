from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^home$', views.home),
    url(r'^message$', views.message),
    url(r'^logout$', views.logout),
    url(r'^comment/(?P<id>\d+)$', views.comment),
    url(r'^test$', views.test),
]