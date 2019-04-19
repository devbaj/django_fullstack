from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.registration_login_forms),
    url(r'^register/process$', views.register),
    url(r'^login/process$', views.login),
    # url(r'^user/(?P<userid>\d+)/home', views.user_home),
    url(r'^logout$', views.logout),
    url(r'^email$', views.check_email),
    url(r'^username$', views.check_username)
]