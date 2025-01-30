from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path('', views.home, name='home'),
    path('create/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
