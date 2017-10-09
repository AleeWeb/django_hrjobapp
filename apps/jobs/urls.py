from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)/edit$',views.edit, name='edit'),
    url(r'^update/(?P<id>\d+)/update$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete')
]