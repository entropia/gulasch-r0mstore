from django import forms
from django.forms import ModelForm

from users.models import User

class UserCreateForm(ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input'}))
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'input'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'twitter', 'github']
		widgets = {
			'username' : forms.TextInput(attrs={'class': 'input'}),
			'email' : forms.TextInput(attrs={'class': 'input'}),
			'twitter' : forms.TextInput(attrs={'class': 'input'}),
			'github' : forms.TextInput(attrs={'class': 'input'}),
		}


	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")

		return password1


	def clean_email(self):
		#Make sure Email is unique
		email = self.cleaned_data.get("email")
		if User.objects.filter(email = email):
			raise forms.ValidationError("Email already in use.")

		return email


	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.is_active = False
		if commit:
			user.save()
		return user



class UserUpdateForm(ModelForm):
	new_password1 = forms.CharField(label='New Password',
									widget=forms.PasswordInput,
									required=False)
	new_password2 = forms.CharField(label='New Password confirmation',
									widget=forms.PasswordInput,
									required=False)
	current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['email', 'twitter', 'github']


	def clean_current_password(self):
		current_password = self.cleaned_data.get("current_password")

		if not self.instance.check_password(current_password):
			raise forms.ValidationError("Password incorrect")

		return current_password


	def clean_new_password2(self):
		password1 = self.cleaned_data.get("new_password1")
		password2 = self.cleaned_data.get("new_password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")

		return password1


	def clean_email(self):
		#Make sure Email is still unique
		email = self.cleaned_data.get("email")
		if User.objects.filter(email = email).exclude(id=self.instance.id):
			raise forms.ValidationError("Email already in use.")

		return email


	def save(self, commit=True):
		user = super(UserUpdateForm, self).save(commit=False)

		password = self.cleaned_data.get("new_password1")
		if password:
			user.set_password(password)

		if commit:
			user.save()
		return user
