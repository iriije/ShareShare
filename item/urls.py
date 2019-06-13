from django.conf.urls import url
from django.urls import path


from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "item"

urlpatterns = [
    url(r'^items/$', views.items, name='items'),
    url(r'^regist/$', views.regist, name='regist'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('<int:item_id>/', views.update, name='item'),
    path('<slug:tag_name>/', views.search_tag),
]
