from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView
)

urlpatterns = [
    path('new/',NoteCreateView.as_view(), name='note-create'),
    path('',views.notes,name='notes'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]