from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^process$', views.process, name = 'process'),
    # url(r'^completed$', views.completed, name = 'completed'),
    url(r'^clear_session$', views.clear_session, name = 'clear_session'),
]
