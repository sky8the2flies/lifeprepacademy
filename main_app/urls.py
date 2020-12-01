
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
    path('d/', views.organization_dashboard, name='org_dashboard'),
    path('wellsfargo', views.wellsfargo_page, name='wellsfargo'),

    # ORGANIZATIONS
    path('organizations/create', views.organization_create, name='org_create'),
    path('organizations/students/create/', views.student_create, name='student_create'),

    # PREPARE
    path('prepare/<int:pg>/', views.prepare_page, name='prepare'),

    # JOURNEY
    path('journey/<int:pg>/', views.journey_page, name='journey'),

    # HEALTHY
    path('healthy/<int:pg>/', views.healthy_page, name='healthy'),

    # SITES
    path('category/<str:category>/', views.site_list, name='site_list')
]
