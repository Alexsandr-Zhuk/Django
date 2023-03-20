from django.urls import path
from my_pr import views

urlpatterns = [
    path("", views.index),
]