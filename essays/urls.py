from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'essays'
urlpatterns = [
    path('', views.index, name='index'),
    path('<pk>/', views.essay, name='essay'),
    url(r'^new$', views.create, name='new'),
    url(r'^edit/(?P<pk>[-\d\w]+)$', views.update, name='update'),
    url(r'^delete/(?P<pk>[-\d\w]+)$', views.delete, name='delete'),
    url(r'^download/(?P<pk>[-\d\w]+)[.](?P<suffix>\w+)$', views.download, name='download'),
    url(r'^download_by$', views.download_by_category, name='dbc')
]