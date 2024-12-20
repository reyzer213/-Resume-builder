from django import forms
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from .models import Profile
from .models import Resume


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'title', 
            'desire_pos', 
            'salary', 
            'first_name', 
            'last_name', 
            'photo', 
            'phone', 
            'email', 
            'experience', 
            'education', 
            'additional_info'
        ]