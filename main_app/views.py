from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.db.models import Q

from accounts.models import User
from accounts.forms import StudentRegister

from .forms import OrganizationForm, StudentForm
from .models import Organization, Administrator, Student, Site

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


def wellsfargo_page(request):
    return render(request, 'main_app/wellsfargo.html')


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
    try:
        student_list = Student.objects.filter(
            admin=admin.id).order_by('student_name')
    except:
        pass  # TODO
    student_form = StudentForm()
    register_form = StudentRegister()

    return render(request, 'main_app/organizations/org_dashboard.html', {
        'student_form': student_form,
        'register_form': register_form,
        'student_list': student_list,
        'admin': admin,
    })


def student_create(request):
    if request.method == 'POST':
        form = StudentRegister(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(student_name=request.POST.get('student_name'),
                                   student_email=request.POST.get(
                                       'username'),
                                   parent_email=request.POST.get(
                                       'parent_email'),
                                   admin_id=request.POST.get('admin_id'),
                                   organization_id=request.POST.get(
                                   'organization_id'),
                                   user_id=user.id
                                   )

            return redirect('org_dashboard')
        # TODO ERROR ON USER FORM
        print('error on user form')
    return redirect('org_dashboard')

# PREPARE

def prepare_page(request, pg):
    return render(request, f'main_app/prepare/prepare_{pg}.html')

# JOURNEY

def journey_page(request, pg):
    return render(request, f'main_app/journey/journey_{pg}.html')

# JOURNEY

def healthy_page(request, pg):
    return render(request, f'main_app/healthy/healthy_{pg}.html')

# SITES

def site_list(request, category):
    sites = []
    try:
        sites = Site.objects.filter(category=category).order_by('site')
    except Site.DoesNotExist:
        pass
    print(sites)
    return render(request, 'main_app/sites/category.html', {
        'sites':sites,
        'category':category.capitalize(),
    })

