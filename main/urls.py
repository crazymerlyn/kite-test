from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
        url('^profile', views.profile, name='profile'),
        url('^signup', views.signup, name='signup'),
        url('^add_investor', views.add_investor, name='add_investor'),
        url('^password_reset/$', auth_views.password_reset, name='password_reset'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                auth_views.password_reset_confirm, name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
        url('^request_token', views.request_token, name='request_token'),
        url('', views.index, name='home'),
]
