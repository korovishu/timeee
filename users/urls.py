from django.urls import path
from .views import (
    DeptUpdateView
)
from . import views

urlpatterns = [
    path('<pk>/update/', DeptUpdateView.as_view(), name='dept-update'),
]