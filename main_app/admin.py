from django.contrib import admin
from .models import Organization, Administrator, Student, Site, Notes

admin.site.register(Organization)
admin.site.register(Administrator)
admin.site.register(Student)
admin.site.register(Site)
admin.site.register(Notes)

