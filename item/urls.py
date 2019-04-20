from django.conf.urls import url

from . import views

app_name = "item"

urlpatterns = [
    url(r'^items/$', views.items, name='items'),
    url(r'^wirte/$', views.write, name='write'),
]