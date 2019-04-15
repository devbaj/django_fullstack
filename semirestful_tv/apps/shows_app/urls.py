from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/new/add$', views.add_new_show),
    url(r'^shows/(?P<show_id>\d+)$', views.display_show),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/edit/process$', views.process_edit),
    url(r'^shows/(?P<show_id>\d+)/delete$', views.remove_show)
]