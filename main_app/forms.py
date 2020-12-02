from django import forms

from .models import Organization, Student


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        labels = {

        }
        fields = [
            'organization_name', 'contact_name', 'contact_title', 'contact_email', 'address', 'city', 'state', 'zip_code',
            'county', 'phone', 'website_url', 'category', 'logo_url', 'promo_code',
        ]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        labels = {
            'student_name': 'Student Name',
        }

        fields = [
            'student_name', 'parent_email',
        ]
