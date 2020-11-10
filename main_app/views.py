from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class HomePageView (TemplateView):
    template_name = "main_app/home.html"

def signup (request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect ("home")
        
    form=UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def contact_page(request):
    return render(request, 'main_app/contact.html')

def intro_page(request):
    return render(request, 'main_app/intro.html')

def pricing_page(request):
    return render(request, 'main_app/pricing.html')

def why_page(request):
    return render(request, 'main_app/why.html')

def prepare_1_page(request):
    return render(request, 'main_app/prepare/prepare_1.html')

def prepare_2_page(request):
    return render(request, 'main_app/prepare/prepare_2.html')

def journey_1_page(request):
    return render(request, 'main_app/journey/journey_1.html')