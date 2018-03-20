from django.conf.urls import url
from . import views

urlpatterns = [
        url('^login', views.login, name='login'),
        url('^request_token', views.request_token, name='login'),
        url('', views.index, name='index'),
]
