
from django.urls import path, include

from . import views

urlpatterns = [
    # GENERAL
    path('', views.HomePageView.as_view(), name="home"),
    path('intro/', views.intro_page, name='intro'),
    path('contact/', views.contact_page, name='contact'),
    path('pricing/', views.pricing_page, name='pricing'),
    path('why/', views.why_page, name='why'),
    path('dashboard/', views.dashboard_page, name='dashboard'),

    # ORGANIZATIONS
    path('organizations/create', views.organization_create, name='org_create'),

    # PREPARE
    path('prepare/prepare_1/', views.prepare_1_page, name='prepare_1'),
    path('prepare/prepare_2/', views.prepare_2_page, name='prepare_2'),

    # JOURNEY
    path('journey/journey_1/', views.journey_1_page, name='journey_1'),

    # AUTH
    path('accounts/signup/', views.signup, name="signup"),
]
