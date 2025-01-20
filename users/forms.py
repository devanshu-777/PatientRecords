from django import forms

class PatientDetailsForm(forms.Form):
    opd_number = forms.CharField(label='OPD Number', max_length=100)
    case_year = forms.CharField(label='Case Year', max_length=100)
    previous_opd_number = forms.CharField(label='Previous OPD Number', max_length=100, required=False)
    previous_case_year = forms.CharField(label='Previous Case Year', max_length=100, required=False)
    name_of_patient = forms.CharField(label='Name of Patient', max_length=200)
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    diagnosis = forms.CharField(label='Diagnosis', widget=forms.Textarea)
    visit_count = forms.IntegerField(label='Visit Count', required=False)
    name_of_user = forms.CharField(label='Name of User', max_length=200)
    academic_year = forms.CharField(label='Academic Year', max_length=100)
    roll_number = forms.CharField(label='Roll Number', max_length=100)