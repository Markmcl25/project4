from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
]
