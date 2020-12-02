from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

from .forms import RegisterForm
from main_app.models import Organization, Administrator


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            promo = request.POST.get('promo_code').upper()
            try:
                organization = Organization.objects.get(promo_code=promo)
            except Organization.DoesNotExist:
                return render(request, 'registration/signup.html', {
                    'form': form,
                    'err': 'Promo code did not match an organization.'
                })
            user = form.save(commit=False)
            user.admin = True
            user.save()
            Administrator.objects.create(
                user_id=user.id, organization_id=organization.id)
            login(request, user)
            return redirect("profile_update")

    form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


class ProfileDetailView(DetailView):
    model = Administrator
    template_name = 'registration/profile/index.html'

    def get_object(self):
        return get_object_or_404(Administrator, user=self.request.user.id)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Administrator
    template_name = 'registration/profile/update.html'
    fields = ['admin_name', 'title', 'email']

    def get_object(self):
        return get_object_or_404(Administrator, user=self.request.user.id)

    def get_success_url(self):
        return reverse('org_dashboard')
