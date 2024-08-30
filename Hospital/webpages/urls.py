from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('hospital/',views.hospital, name='hospital'),
    path('contact/',views.contact, name='contact'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
]