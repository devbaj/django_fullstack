from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration/process$', views.process_reg),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^login/process$', views.login)
]