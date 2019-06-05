from django.urls import path
from django.conf.urls import url
from . import views

app_name = "rent"

urlpatterns = [
    #url(r'(?P<item_id>\d+)/$', views.rent, name='rent'),
    path('<int:item_id>/', views.rent, name='rent'),
]