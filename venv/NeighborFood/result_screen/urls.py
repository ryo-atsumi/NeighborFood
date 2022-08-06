from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ResultList.as_view(), name="result"),
]