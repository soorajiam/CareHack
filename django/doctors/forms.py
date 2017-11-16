from django import forms
from .models import Appointment
from django.core.exceptions import ValidationError

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['time', 'time_zone',]