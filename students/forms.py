from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('fullname','birthday','gender','classname','address','avatar','phone','specialization')
        