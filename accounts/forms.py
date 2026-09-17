from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PatientProfile, Diagnosis


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class QuestionnaireForm(forms.ModelForm):
    diagnosis = forms.ModelChoiceField(
        queryset=Diagnosis.objects.all(),
        empty_label='Select your injury/condition',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    pain_level = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'class': 'form-range pain-slider',
            'min': '1',
            'max': '10',
        }),
    )
    surgery_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    class Meta:
        model = PatientProfile
        fields = ['diagnosis', 'pt_status', 'current_facility', 'had_surgery', 'surgery_date', 'pain_level']
        widgets = {
            'pt_status': forms.Select(attrs={'class': 'form-select'}),
            'current_facility': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your PT facility'}),
            'had_surgery': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
