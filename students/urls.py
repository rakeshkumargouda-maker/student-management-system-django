from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, 
        name="dashboard"),
    path("addstudent/", views.addstudent, 
        name="addstudent"),
    path("viewstudents/", views.viewstudents,
        name="viewstudents")
]
