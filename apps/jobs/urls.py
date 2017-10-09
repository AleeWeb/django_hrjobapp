from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<id>\d+)/edit$',views.edit, name='edit'),
    url(r'^(?P<id>\d+)/update$', views.update, name='update'),
    url(r'^(?P<id>\d+)/show$', views.show, name='show'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete')
]