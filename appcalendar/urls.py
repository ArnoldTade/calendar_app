from appcalendar import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    # path("dashboard/<int:id>", views.dashboard, name="dashboard"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("viewBook/<int:id>", views.viewBook, name="viewBook"),
]
