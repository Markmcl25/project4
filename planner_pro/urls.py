from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup

urlpatterns = [
    # Homepage (Upcoming Events)
    path("", views.home, name="home"),

    # Authentication
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Event Management
    path("create-event/", views.create_event, name="create_event"),  # Requires login
    path("events/", views.event_list, name="event_list"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),  # Individual Event Page

    # User Dashboard (Requires Login)
    path("dashboard/", views.dashboard, name="dashboard"),
]
