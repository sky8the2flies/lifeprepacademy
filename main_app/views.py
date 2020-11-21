from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from .forms import OrganizationForm
from .models import Organization

class HomePageView (TemplateView):
    template_name = "main_app/home.html"

def signup (request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect ("dashboard")
        
    form=UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

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
    if not request.user.promo_code:
        return redirect('login')
    try:
        organization=Organization.objects.get(promo_code=request.user.promo_code)
    except:
        return redirect('login')

    return render(request, 'main_app/organizations/org_dashboard.html', {'organization':organization})

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
def journey_12_page(request):
    return render(request, 'main_app/journey/journey_12.html')