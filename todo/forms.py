from django import forms

from .models import AddTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
