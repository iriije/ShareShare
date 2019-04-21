from django.conf.urls import url

from . import views

app_name = "item"

urlpatterns = [
    url(r'^item/$', views.items, name='items'),
    url(r'^regist/$', views.regist, name='regist'),
]