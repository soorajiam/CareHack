from django.conf.urls import url
from doctors import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^view/$', views.view_doctors, name='view_doctors'),
    url(r'^view/(?P<pk>\d+)$', views.view_doctor, name='view_doctor'),
    url(r'^view/(?P<pk>\d+)/getapp', views.create_appointment, name='create_appointment'),



]
