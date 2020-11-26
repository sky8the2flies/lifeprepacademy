
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

    # ORGANIZATIONS
    path('organizations/create', views.organization_create, name='org_create'),
    path('organizations/students/create/', views.student_create, name='student_create'),

    # PREPARE
    path('prepare/prepare_1/', views.prepare_1_page, name='prepare_1'),
    path('prepare/prepare_2/', views.prepare_2_page, name='prepare_2'),
    path('prepare/prepare_3/', views.prepare_3_page, name='prepare_3'),
    path('prepare/prepare_4/', views.prepare_4_page, name='prepare_4'),
    path('prepare/prepare_5/', views.prepare_5_page, name='prepare_5'),
    path('prepare/prepare_6/', views.prepare_6_page, name='prepare_6'),
    path('prepare/prepare_7/', views.prepare_7_page, name='prepare_7'),
    path('prepare/prepare_8/', views.prepare_8_page, name='prepare_8'),
    path('prepare/prepare_9/', views.prepare_9_page, name='prepare_9'),

    # JOURNEY
    path('journey/journey_1/', views.journey_1_page, name='journey_1'),
    path('journey/journey_2/', views.journey_2_page, name='journey_2'),
    path('journey/journey_3/', views.journey_3_page, name='journey_3'),
    path('journey/journey_4/', views.journey_4_page, name='journey_4'),
    path('journey/journey_5/', views.journey_5_page, name='journey_5'),
    path('journey/journey_6/', views.journey_6_page, name='journey_6'),
    path('journey/journey_7/', views.journey_7_page, name='journey_7'),
    path('journey/journey_8/', views.journey_8_page, name='journey_8'),
    path('journey/journey_9/', views.journey_9_page, name='journey_9'),
    path('journey/journey_10/', views.journey_10_page, name='journey_10'),
    path('journey/journey_11/', views.journey_11_page, name='journey_11'),
    path('journey/journey_12/', views.journey_12_page, name='journey_12'),
    path('journey/journey_13/', views.journey_13_page, name='journey_13'),
    path('journey/journey_14/', views.journey_14_page, name='journey_14'),
    path('journey/journey_15/', views.journey_15_page, name='journey_15'),
    path('journey/journey_16/', views.journey_16_page, name='journey_16'),
    path('journey/journey_17/', views.journey_17_page, name='journey_17'),
    path('journey/journey_18/', views.journey_18_page, name='journey_18'),
    path('journey/journey_19/', views.journey_19_page, name='journey_19'),
    path('journey/journey_20/', views.journey_20_page, name='journey_20'),
]
