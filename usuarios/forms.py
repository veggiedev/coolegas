from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
import datetime

# Create your forms here.
today = datetime.date.today()

year = today.year
old_enough = year - 18
date = 1901
dates_list = [1900, 1901]
for i in range (250):
	if dates_list[-1] < old_enough:
		date += 1
		dates_list.append(date)


class NewUserForm(UserCreationForm):
	# def __init__(self, *args, **kwargs):
	# 	super(NewUserForm, self).__init__(*args, **kwargs)

	# 	for fieldname in ['username', 'password1', 'password2']:
	# 		self.fields[fieldname].help_text = None
	username = forms.CharField(label='Nombre de Usuario', max_length='30', required='True')
	first_name = forms.CharField(label='Nombre',max_length=30, required=True, help_text='*')
	last_name = forms.CharField(label='Apellidos',max_length=30, required=True, help_text='*')
	birthdate = forms.DateField(widget=forms.SelectDateWidget(years=reversed(dates_list)), label='Nacimiento', required=True, help_text='*')
	email = forms.EmailField(label='Correo Electrónico',max_length=254, help_text='*')
	password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(), help_text='<br>La contraseña debe contener mayúsculas y letras. Debe ser difícil de adivinar.')
	password2 = forms.CharField(label='Repita Contraseña',widget=forms.PasswordInput(), help_text='<br>Confirma la contraseña por favor.')

	# confirm_password=forms.CharField(label='Confirma la contraseña',widget=forms.PasswordInput(), help_text='*')
	# nacimiento = forms.DateField(null=True,verbose_name=('Fecha de nacimiento (dd/mm/aaaa)'))
	# fecha_creacion  = forms.DateField(verbose_name=('Fecha cuenta creada'), auto_now_add=True)
	
	class Meta():
		model = User
		fields = ['username','first_name', 'last_name', 'birthdate', 'email']
	
	# def clean(self):
	# 	cleaned_data = super(UserForm, self).clean()
	# 	password = cleaned_data.get("password")
	# 	confirm_password = cleaned_data.get("confirm_password")

	# 	if password != confirm_password:
	# 		raise forms.ValidationError(
	# 			"Las contraseñas no coinciden"
	# 		)

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class UserProfileForm(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = ('provincia', 'ciudad')






class login_form(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ['email', 'password']

