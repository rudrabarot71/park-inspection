# In your forms.py file

from django import forms
from .models import Inspection

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['park_name', 'park_location', 'park_description', 'inspector_name', 'inspector_email', 'date_inspected', 'inspection_notes', 'is_passed']

        widgets = {
            'date_inspected': forms.DateInput(attrs={'type': 'date'}),
        }