from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = [
            'name',
            'phone',
            'email',
            'location',
            'device_type',
            'issue_description',
            'best_time_to_contact',
        ]

        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'location': 'City / Area',
            'device_type': 'Device Type',
            'issue_description': 'Describe the Issue',
            'best_time_to_contact': 'Best Time to Contact You',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'location': forms.TextInput(attrs={'placeholder': 'Example: Plainfield, Camby, Indianapolis'}),
            'issue_description': forms.Textarea(attrs={
                'placeholder': 'Tell me what problem you are having...',
                'rows': 5
            }),
            'best_time_to_contact': forms.TextInput(attrs={'placeholder': 'Example: After 5 PM or Saturday morning'}),
        }