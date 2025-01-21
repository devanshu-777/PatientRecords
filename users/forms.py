from django import forms
import datetime

current_date = datetime.datetime.now()
current_month = current_date.month

if current_month <= 3:  # January to March
    current_year = current_date.year - 1
else:  # April to December
    current_year = current_date.year
    
academic_year_choices = [(f"{year}-{year + 1}", f"{year}-{year + 1}") for year in range(current_year - 5, current_year + 6)]
default_academic_year = f"{current_year}-{current_year + 1}"

class PatientDetailsForm(forms.Form):
    opd_number = forms.CharField(label='OPD Number', max_length=100)
    case_year = forms.CharField(label='Case Year', max_length=100)
    previous_opd_number = forms.CharField(label='Previous OPD Number', max_length=100, required=False)
    previous_case_year = forms.CharField(label='Previous Case Year', max_length=100, required=False)
    name_of_patient = forms.CharField(label='Name of Patient', max_length=200)
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    diagnosis = forms.CharField(label='Diagnosis', max_length=200)
    peripheral_opd = forms.CharField(label='Peripheral OPD Name', required=False)
    name_of_intern = forms.CharField(label='Name of Intern', max_length=200)
    academic_year = forms.ChoiceField(label="Academic Year", choices=academic_year_choices, initial=default_academic_year, required=False)
    roll_number = forms.CharField(label='Roll Number', max_length=100)