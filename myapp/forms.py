from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_title', 'company_name', 'description', 'openings', 'location', 'contact_email']
