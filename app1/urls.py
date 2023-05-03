from . import views
from django.urls import path

urlpatterns = [
    path("", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("entry", views.add_entry, name="entry"),
    path("logout", views.logout, name="logout"),
]
