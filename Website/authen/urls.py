from django.conf.urls import url
from authen import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^sendpin/', views.send_pin, name='send_pin'),
    url(r'^register/', views.register, name='register'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^login/', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/authen'}, name='logout'),

]
