from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', views.signup, name='signup')
]