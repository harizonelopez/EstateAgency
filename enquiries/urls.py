from django.urls import path
from . import views

app_name = 'enquiries'

urlpatterns = [
    path('', views.contact, name='contact'),
]

