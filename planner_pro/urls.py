from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup, custom_logout

urlpatterns = [
    # Homepage (Upcoming Events)
    path("", views.home, name="home"),

    # Authentication
    path("profile/", views.profile, name="profile"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", custom_logout, name="logout"),

    # Event Management
    path('host-event/', views.create_event, name='host-event'),
    path("create-event/", views.create_event, name="create_event"),  # Requires login
    path("events/", views.event_list, name="event_list"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),  # Individual Event Page
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),  # Event Edit
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'), # Event Delete

    # User Dashboard (Requires Login)
    path("dashboard/", views.dashboard, name="dashboard"),

    path('pending-bookings/', views.pending_bookings, name='pending_bookings'),

]

