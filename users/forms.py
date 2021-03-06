from django.contrib.auth.models import User 	
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Profile

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = (
			'photo', 'birth_date'
		)