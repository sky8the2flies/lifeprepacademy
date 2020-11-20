from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

from main_app.models import Organization, Administrator


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            promo = request.POST.get('promo_code')
            try:
                organization = Organization.objects.get(promo_code=promo)
            except Organization.DoesNotExist:
                return render(request, 'registration/signup.html', {
                    'form': form,
                    'err': 'Promo code did not match an organization.'
                })
            user = form.save()
            Administrator.objects.create(
                user_id=user.id, organization_id=organization.id)
            login(request, user)
            return redirect("dashboard")

    form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})
