from django.contrib import admin
from django.urls import path, include
from . import views as timetable_views



urlpatterns = [
    path('home/',timetable_views.home, name='home'),
]
