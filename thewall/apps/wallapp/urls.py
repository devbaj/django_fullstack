from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.wall),
    url(r'message/send$', views.send_message),
    url(r'comment/send$', views.send_comment)
]