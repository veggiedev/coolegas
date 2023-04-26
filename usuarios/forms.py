from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import UserProfile, Actividades
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
	username = forms.CharField(label='Nombre de usuario', max_length=30, required=True)
	first_name = forms.CharField(label='Nombre',max_length=30, required=True)
	last_name = forms.CharField(label='Apellidos',max_length=30, required=True)
	birthdate = forms.DateField(widget=forms.SelectDateWidget(years=reversed(dates_list)), label='Nacimiento', required=True)
	email = forms.EmailField(label='Correo', max_length=254, required=True, )
	password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(), required=True)
	# password2 = forms.CharField(label='Repita Contraseña',widget=forms.PasswordInput(), help_text='Confirma la contraseña por favor.<br>La contraseña debe contener mayúsculas y letras. Debe ser difícil de adivinar.', required=True)

	class Meta():
		model = User
		fields = ['username', 'first_name', 'last_name', 'birthdate', 'email']
	
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	



class actividades_form(forms.ModelForm):
	actividades = ['Ciclismo', 'Correr', 'Natación', 'Senderismo', 'Caminar', 
                   'Pasear', 'Bicicleta', 'Caminata', 'Netflix', 'Cine', 
                   'Cocinar', 'Comer', 'Bailar', 'Fútbol', 'Baloncesto', 
                   'Tenis', 'Voleibol', 'Ping Pong', 'Ajedrez', 'Bar', 'Café', 
                   'Cerveza', 'Cena', 'Cóctel', 'Comida', 'Desayuno', 'Picnic', 
                   'Pintxos', 'Vino', 'Yoga', 'Meditación', 'Pilates', 'Spinning', 
                   'Crossfit', 'Gimnasio', 'Piscina', 'Paseo', 'Caminata', 
                   'Camping']
	actividad = models.CharField(choices=[(actividad, actividad) for actividad in actividades], max_length=264)
	descripcion = models.CharField(max_length=264)
	fecha_inicio = models.DateTimeField()
	fecha_fin = models.DateTimeField()

	class Meta():
		model = Actividades
		fields = ['actividad', 'descripcion', 'fecha_inicio', 'fecha_fin', 'provincia', 'ciudad']
		widgets = {
			'fecha_inicio': forms.SelectDateWidget(years=reversed(dates_list)),
			'fecha_fin': forms.SelectDateWidget(years=reversed(dates_list)),

		}






class login_form(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ['username', 'password']

