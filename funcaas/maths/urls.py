from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^is/int/(.+)/$', views.is_int),
    url(r'^docs/$', views.docs),
]
