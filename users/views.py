from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import PatientDetailsForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def login_view(request):
    # Handle displaying messages
    return render(request, "index.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("/")

@login_required
def submit_patient_details(request):
    if request.method == 'POST':
        form = PatientDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract patient details
            patient_details = form.cleaned_data

            # Handle image uploads
            images = request.FILES.getlist('patient_images')
            # Prepare email content
            email_subject = f"{patient_details['name_of_patient']} - {patient_details['opd_number']} /{patient_details['case_year']} - {patient_details['diagnosis']} /{patient_details.get('peripheral_opd', 'N/A')}"
            email_message = (
                f"OPD Number: {patient_details['opd_number']}\n"
                f"Case Year: {patient_details['case_year']}\n"
                f"Previous OPD Number: {patient_details.get('previous_opd_number', 'N/A')}\n"
                f"Previous Case Year: {patient_details.get('previous_case_year', 'N/A')}\n"
                f"Name of Patient: {patient_details['name_of_patient']}\n"
                f"Age: {patient_details['age']}\n"
                f"Gender: {patient_details['gender']}\n"
                f"Diagnosis: {patient_details['diagnosis']}\n"
                f"Peripheral OPD Name: {patient_details.get('peripheral_opd', 'N/A')}\n"
                f"Name of Intern: {patient_details['name_of_intern']}\n"
                f"Academic Year: {patient_details['academic_year']}\n"
                f"Roll Number: {patient_details['roll_number']}"
            )

            recipient_list = ['cases2.ahmc@gmail.com']

            # Send the email with patient details and images attached
            email = EmailMessage(email_subject, email_message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            for img in images:
                email.attach(img.name, img.read(), img.content_type)
            email.send()

            messages.success(request, 'Details and images submitted and email sent successfully!')
            return redirect('/')
    else:
        form = PatientDetailsForm()

    return render(request, 'patient_form.html', {'form': form})