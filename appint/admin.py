from django.contrib import admin
from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('namef', 'mobile',  'email',  'city', 'day')
    list_display_links = ('namef', 'mobile',  'email', 'city', 'day')


admin.site.register(Appointment, ContactAdmin)

# full_name = models.CharField(max_length=100)
# gender = models.CharField(max_length=50)
# mobile = models.CharField(max_length=50)
# day = models.CharField(max_length=50)
# month = models.CharField(max_length=50)
# year = models.CharField(max_length=50)
# address = models.CharField(max_length=200)
# address2 = models.CharField(max_length=200)
# city = models.CharField(max_length=100)
# state = models.CharField(max_length=100)
# zipcode = models.CharField(max_length=50)
# country = models.CharField(max_length=50)
# email = models.EmailField(max_length=50)
# textarea = models.CharField(max_length=1000)