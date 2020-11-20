
from django.urls import path, include

from . import views

urlpatterns = [
    # AUTH
    path('accounts/signup/', views.signup, name="signup"),
]
