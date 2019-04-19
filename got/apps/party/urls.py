from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.display_events),
    url(r'^events/(?P<eventid>\d+)$', views.display_one_event),
    url(r'^/event/destroy$', views.destroy_event),
    url(r'^/dashboard$', views.dashboard),
    url(r'^/create$', views.create_event_form),
    url(r'^/show/add$', views.add_show)
]