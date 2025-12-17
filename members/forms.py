from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length= 100)
	last_name = forms.CharField(max_length= 100)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class EditProfileForm(UserChangeForm):
	username = forms.CharField(max_length=100)
	email = forms.EmailField()
	first_name = forms.CharField(max_length= 100)
	last_name = forms.CharField(max_length= 100)
	# last_login = forms.CharField(max_length= 100)
	# is_superuser = forms.CharField(max_length= 100)
	# is_staff = forms.CharField(max_length= 100)
	# is_active = forms.CharField(max_length= 100)	
	# date_joined = forms.CharField(max_length= 100)


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')