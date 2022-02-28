from django import forms
from .models import *

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['fname', 'lname', 'tech', 'email', 'photo' ] 
