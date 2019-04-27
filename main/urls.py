from django.urls import path
from django.conf.urls import url
from item import views

urlpatterns = [
	url(r'^$', views.SearchFormView.as_view(), name='index'),
]