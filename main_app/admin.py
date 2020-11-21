from django.contrib import admin
from .models import Organization, Administrator, Student

admin.site.register(Organization)
admin.site.register(Administrator)
admin.site.register(Student)
