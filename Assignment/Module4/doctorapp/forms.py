from django import forms
from .models import *

class doc(forms.ModelForm):
    class Meta:
        model = Doctor
        fields='__all__'