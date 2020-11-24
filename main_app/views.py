from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.db.models import Q

from .forms import OrganizationForm, StudentForm
from .models import Organization, Administrator, Student


class HomePageView (TemplateView):
    template_name = "main_app/home.html"


def contact_page(request):
    return render(request, 'main_app/contact.html')


def dashboard_page(request):
    return render(request, 'main_app/dashboard.html')


def intro_page(request):
    return render(request, 'main_app/intro.html')


def pricing_page(request):
    return render(request, 'main_app/pricing.html')


def why_page(request):
    return render(request, 'main_app/why.html')

# ORGANIZATIONS


def organization_create(request):
    org_form = OrganizationForm()
    return render(request, 'main_app/organizations/create.html', {
        'org_form': org_form
    })


def organization_dashboard(request):
    if not request.user.id:
        return redirect('login')
    try:
        admin = Administrator.objects.get(user=request.user.id)
    except Administrator.DoesNotExist:
        # TODO admin not found
        return redirect('login')
    student_form = StudentForm()

    return render(request, 'main_app/organizations/org_dashboard.html', {
        'student_form': student_form,
        'admin': admin,
    })
# <QueryDict: {'csrfmiddlewaretoken': ['iJQx29qrimwalp9JyC20BofqtCLxVPSZB2w0PjBwwyJpIJERTlBCoaM7KAkb8UkF'], 'student_name': ['Devin2'], 'student_email': ['devin2@gmail.com'], 'parent_email': ['parent@gmail.com'], 'password': ['aabbcc123'], 'admin': ['Devin'], 'organization': ['Crenshaw High'], 'next': ['']}>


def student_create(request):
    if request.method == 'POST':
        Student.objects.create(student_name=request.POST.get('student_name'),
        student_email=request.POST.get('student_email'),
        parent_email=request.POST.get('parent_email'),
        password=request.POST.get('password'),
        admin_id=request.POST.get('admin_id'),
        organization_id=request.POST.get('organization_id')
        )

        return redirect('org_dashboard')
    return redirect('org_dashboard') 


# PREPARE


def prepare_1_page(request):
    return render(request, 'main_app/prepare/prepare_1.html')
def prepare_2_page(request):
    return render(request, 'main_app/prepare/prepare_2.html')
def prepare_3_page(request):
    return render(request, 'main_app/prepare/prepare_3.html')
def prepare_4_page(request):
    return render(request, 'main_app/prepare/prepare_4.html')
def prepare_5_page(request):
    return render(request, 'main_app/prepare/prepare_5.html')
def prepare_6_page(request):
    return render(request, 'main_app/prepare/prepare_6.html')
def prepare_7_page(request):
    return render(request, 'main_app/prepare/prepare_7.html')
def prepare_8_page(request):
    return render(request, 'main_app/prepare/prepare_8.html')
def prepare_9_page(request):
    return render(request, 'main_app/prepare/prepare_9.html')

# JOURNEY

def journey_1_page(request):
    return render(request, 'main_app/journey/journey_1.html')
def journey_2_page(request):
    return render(request, 'main_app/journey/journey_2.html')
def journey_3_page(request):
    return render(request, 'main_app/journey/journey_3.html')
def journey_4_page(request):
    return render(request, 'main_app/journey/journey_4.html')
def journey_5_page(request):
    return render(request, 'main_app/journey/journey_5.html')
def journey_6_page(request):
    return render(request, 'main_app/journey/journey_6.html')
def journey_7_page(request):
    return render(request, 'main_app/journey/journey_7.html')
def journey_8_page(request):
    return render(request, 'main_app/journey/journey_8.html')
def journey_9_page(request):
    return render(request, 'main_app/journey/journey_9.html')
def journey_10_page(request):
    return render(request, 'main_app/journey/journey_10.html')
def journey_11_page(request):
    return render(request, 'main_app/journey/journey_11.html')
def journey_12_page(request):
    return render(request, 'main_app/journey/journey_12.html')
def journey_13_page(request):
    return render(request, 'main_app/journey/journey_13.html')
