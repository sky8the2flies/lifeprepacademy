
from django.urls import path, include

from . import views

urlpatterns = [
    # AUTH
    path('accounts/signup/', views.signup, name="signup"),

    # PROFILE
    path('accounts/profile/', views.ProfileDetailView.as_view(), name="profile"),
    path('accounts/profile/update/',
         views.ProfileUpdateView.as_view(), name="profile_update"),
]
