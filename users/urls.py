from django.urls import path
from django.shortcuts import redirect
from .views import index, submit_patient_details, logout_view

def custom_404_view(request, exception=None):
    return redirect('/')

urlpatterns = [
    path("", index, name="index"),
    path("logout", logout_view, name="logout"),
    path('submit-patient-details/', submit_patient_details, name='submit_patient_details'),
]