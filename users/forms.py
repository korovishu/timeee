from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from .models import Profile

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(max_length=100)


	class Meta(User):
		model = User
		fields =  ['username', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):


	class Meta(User):
		model = User
		fields =  ['username']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image','Roll_No','Department']

