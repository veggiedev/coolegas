from django.db import models
from datetime import date
from django import forms
# Create your models here.
import os
import pandas
from unidecode import unidecode
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

 
 #----------------------------------logic functions--------------------------------------------#

# dir_path = r'templates/buscoAmigosApp/provincias'
dir_path = r'templates/coolegasApp/provincias'

lista_provs = []


for i in range(len(os.listdir(dir_path))):
    lista_provs.append((os.listdir(dir_path)[i].removesuffix('.csv'), os.listdir(dir_path)[i].removesuffix('.csv').capitalize()))

provincias_ordenadas = sorted(lista_provs)

provincia_csv = pandas.read_csv(f'templates/coolegasApp/otros/Municipios.csv')

lista_municipios = provincia_csv.Texto.to_list()
# print(lista_municipios)

municipios_lista_tuples = []

for i in range(len(lista_municipios)):
    if str(lista_municipios[i]) != 'nan':
        
        municipios_lista_tuples.append((str(unidecode(lista_municipios[i])), str(lista_municipios[i])))

municipios_ordenados = sorted(municipios_lista_tuples)
# print(municipios_ordenados[:5])


# print(lista_municipios)
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        lista_provs.append(path.removesuffix('.csv'))

        # provincias_ordenadas = sorted(lista_provs)

# # lista_municipios = 
today = date.today()
today_formated = today.strftime("%Y-%m-%d")

 #----------------------------------end of logic functions--------------------------------------------#


@login_required
class Actividades(models.Model):
    actividades = ['Ciclismo', 'Correr', 'Natación', 'Senderismo', 'Caminar', 
                   'Pasear', 'Bicicleta', 'Caminata', 'Netflix', 'Cine', 
                   'Cocinar', 'Comer', 'Bailar', 'Fútbol', 'Baloncesto', 
                   'Tenis', 'Voleibol', 'Ping Pong', 'Ajedrez', 'Bar', 'Café', 
                   'Cerveza', 'Cena', 'Cóctel', 'Comida', 'Desayuno', 'Picnic', 
                   'Pintxos', 'Vino', 'Yoga', 'Meditación', 'Pilates', 'Spinning', 
                   'Crossfit', 'Gimnasio', 'Piscina', 'Paseo', 'Caminata', 
                   'Camping']
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    actividad = models.CharField(choices=[(actividad, actividad) for actividad in actividades], max_length=264)
    descripcion = models.CharField(max_length=264, null=True)
    fecha_inicio = models.DateTimeField(default=today_formated)
    fecha_fin = models.DateTimeField(default=today_formated)
    provincia = models.CharField(choices=provincias_ordenadas, default='A Coruna', null=True,verbose_name=('Provincia'),max_length=264, unique=False)
    ciudad = models.CharField(choices=municipios_ordenados, default='Ababuj', null=True,verbose_name=('Ciudad'),max_length=264,unique=False)


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_name = models.CharField(null=False,verbose_name=('Nombre completo'),max_length=264,unique=False)   
    # email = models.EmailField(null=True,verbose_name=('Correo electronico'),max_length=264,unique=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil', blank=True)
    # nacimiento = models.DateField(null=True,verbose_name=('Fecha de nacimiento (dd/mm/aaaa)'),)
    fecha_creacion  = models.DateField(verbose_name=('Fecha cuenta creada'), auto_now_add=True)
    # password = models.CharField(max_length=50)
    genero = models.CharField(null=True,verbose_name=('Genero'),max_length=64,unique=False)
    provincia = models.CharField(choices=provincias_ordenadas, default='A Coruna', null=True,verbose_name=('Provincia'),max_length=264, unique=False)
    ciudad = models.CharField(choices=municipios_ordenados, default='Ababuj', null=True,verbose_name=('Ciudad'),max_length=264,unique=False)
    disponibilidad = models.CharField(null=True,max_length=264,unique=False)
    lugar_comida = models.CharField(null=True,max_length=264,unique=False)
    musica = models.CharField(null=True,max_length=264,unique=False)
    musica_relax = models.CharField(null=True,max_length=264,unique=False)
    musica_animada = models.CharField(null=True,max_length=264,unique=False)
    salir = models.CharField(null=True,max_length=264,unique=False)
    actividades = models.CharField(null=True,max_length=264,unique=False)
    latitud = models.CharField(null=True,max_length=264,unique=False)
    longitud = models.CharField(null=True,max_length=264,unique=False)
    

    

# class Actividades(models.Model):
#     actividad = models.CharField(null=True,max_length=264,unique=False)
#     latitud = models.CharField(null=True,max_length=264,unique=False)
#     longitud = models.CharField(null=True,max_length=264,unique=False)
#     invitados = models.CharField(null=True,max_length=264,unique=False)


