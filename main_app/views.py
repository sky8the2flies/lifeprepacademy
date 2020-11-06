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