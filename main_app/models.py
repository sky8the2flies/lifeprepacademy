from django.db import models
from django.contrib.auth.models import User

from phone_field import PhoneField

STATES = (
    ('AL', 'Alabama'),('AK', 'Alaska'),('AS', 'American Samoa'),
    ('AZ', 'Arizona'),('AR', 'Arkansas'),('CA', 'California'),
    ('CO', 'Colorado'),('CT', 'Connecticut'),('DR', 'Deleware'),
    ('DC', 'District of Columbia'),('FL', 'Florida'),('GA', 'Georgia'),
    ('GU', 'Guam'),('HI', 'Hawaii'),('ID', 'Idaho'),
    ('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),
    ('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),
    ('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),
    ('MI', 'Michigan'),('MN', 'Minnesota'),('MS', 'Mississippi'),
    ('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),
    ('NV', 'Nevada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),
    ('ND', 'North Dakota'),('OH', 'Ohio'),('OK', 'Oklahoma'),
    ('OR', 'Oregon'),('PA', 'Pennsylvania'),('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),('SC', 'South Carolina'),('SD', 'South Dakota'),
    ('TN', 'Tennessee'),('TX', 'Texas'),('UT', 'Utah'),
    ('VT', 'Vermont'),('VA', 'Virginia'),('VI', 'Virgin Islands'),
    ('WA', 'Washington'),('WV', 'West Virginia'),('WI', 'Wisconsin'),('WY', 'Wyoming')
)

CATEGORIES = (
    ('EL', 'Elementary School'), ('MD', 'Middle School'), ('HS', 'High School'), ('NP', 'Nonprofit'), ('CH', 'Church')
)

class Organization (models.Model):
    name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    contact_title = models.CharField(max_length=200)
    contact_email = models.EmailField(('email address'))
    address = models.CharField(max_length=200)
    city =  models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATES)
    zip_code = models.CharField(max_length=10)
    county = models.CharField(max_length=200)
    phone = PhoneField(blank=True, help_text='Org. Contact Phone')
    website_url = models.CharField(max_length=200)
    category = models.CharField(max_length=2, choices=CATEGORIES)
    logo_url = models.CharField(max_length = 200, default='https://www.resetyourbody.com/wp-content/uploads/COMPANY_LOGO/logo-default.png', blank='True')
    promo_code = models.CharField(max_length=200)

    admin=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Administrator (models.Model):
    admin = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    admin_email = models.EmailField(('email address'))
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin

class Student (models.Model):
    student = models.CharField(max_length=200)
    student_email = models.EmailField(('email address'))
    parent_email = models.EmailField(('email address'))
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student

class Notes (models.Model):
    note = models.CharField(max_length=2000)

    def __str__(self):
        return self.note

class FavSites (models.Model):
    site = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=200)
    logo_url = models.CharField(max_length=200)

    def __str__(self):
        return self.site