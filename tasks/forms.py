from django import forms
from django.forms import ModelForm, TextInput

from .models import *

class TaskForm(forms.ModelForm):

    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Add a new task ...'}))

    class Meta:
        model = Task
        fields = '__all__'