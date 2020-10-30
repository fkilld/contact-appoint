from django.urls import path
from .views import *

app_name = 'appint'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('appointment/', appointment, name='appointment')
]
