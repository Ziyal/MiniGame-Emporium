from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^guess_letter$', views.guess_letter, name = 'guess_letter'),
    url(r'^reset$', views.reset, name = 'reset')
]
