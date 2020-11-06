
from django.urls import path, include

from . import views

urlpatterns = [
    # GENERAL
    path('', views.HomePageView.as_view(), name="home"),
]
