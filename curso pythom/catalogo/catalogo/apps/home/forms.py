from django import forms
from django.contrib.auth.models import User

class  contact_form(forms.Form):
	correo = forms.EmailField(widget = forms.TextInput())
	titulo = forms.CharField(widget = forms.TextInput())
	texto = forms.CharField(widget = forms.Textarea())

class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave   = forms.CharField(widget = forms.PasswordInput(render_value = False))

class RegisterForm(forms.Form):
	username = forms.CharField(label ="Nombre de Usuario",widget = forms.TextInput())
	email    = forms.EmailField(label = "Correo Electronico",widget = forms.TextInput())
	password_one = forms.CharField(label = "password",widget = forms.PasswordInput(render_value = False))
	password_two = forms.CharField(label = "confirmar password",widget = forms.PasswordInput(render_value = False))

def clean_username(self):
	username = self.clean_data['username']
	try:
		u = User.objects.get(username=username)
	except User.DoesNotExist:
		return username
	raise forms.ValidationError('Nombre de usuario ya existe')

def clean_email(self):
	email = self.clean_data['email']
	try:
		u = User.objects.get(email=email)
	except User.DoesNotExist:
		return email
	raise forms.ValidationError('Email ya Registrado')

def clan_password_two(self):
	password_one = self.clean_data['password_one']
	password_two = self.clean_data['password_two']
	if password_one == password_two:
		pass
	else:
		raise forms.ValidationError('Password no coincide')