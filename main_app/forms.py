from django.forms import ModelForm

from .models import Organization

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        labels = {
            
        }
        fields = [
            'organization_name', 'contact_name', 'contact_title', 'contact_email', 'address', 'city', 'state', 'zip_code',
            'county', 'phone', 'website_url', 'category', 'logo_url', 'promo_code',
        ]