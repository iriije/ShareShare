from django.urls import path
from django.conf.urls import url
from . import views

app_name = "rent"

urlpatterns = [
    url(r'(?P<item>\d+)/$', views.rent, name='rent'),
]