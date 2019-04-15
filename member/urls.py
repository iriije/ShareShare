from django.conf.urls import url

from . import views

app_name = "member"

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^items/$', views.items, name='items'),
    url(r'^wirte/$', views.write, name='write'),
]