from django.urls import path
from .views import index, submit_patient_details, logout_view

urlpatterns = [
    path("", index, name="index"),
    path("logout", logout_view, name="logout"),
    path('submit-patient-details/', submit_patient_details, name='submit_patient_details'),
    # path('upload-images/', upload_images, name='upload_images'),
]