from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import random
from django.contrib.auth import get_user_model
from .forms import NewUserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required




user = get_user_model()


# Create your views here.



def index(request):
    return render(request, 'home.html')

# def signup(request):
#     user_form = NewUserForm()
#     return render(request, 'signup.html', {'user_form':user_form})

def pagina_registro(request):
    if request.method == "POST":
        user_form = NewUserForm(request.POST)
        if user_form.is_valid():
            print(user_form)
            user = user_form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("coolegasApp:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    user_form = NewUserForm()
    return render (request, "signup.html", context={"user_form":user_form})




def about(request):
    return render(request, 'about.html')    


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"You are now logged in as {username}.")
                return redirect("login.html")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", context={"login_form":form})
 
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create a view for the user, where there is a list of activities available to the user to choose from and add that activitie to the users profile. the activity should have a start date and time and a finish date and time
def user_activities(request):
    #create a list of activities
    actividades = ['Ciclismo', 'Correr', 'Natación', 'Senderismo', 'Caminar', 
                   'Pasear', 'Bicicleta', 'Caminata', 'Netflix', 'Cine', 
                   'Cocinar', 'Comer', 'Bailar', 'Fútbol', 'Baloncesto', 
                   'Tenis', 'Voleibol', 'Ping Pong', 'Ajedrez', 'Bar', 'Café', 
                   'Cerveza', 'Cena', 'Cóctel', 'Comida', 'Desayuno', 'Picnic', 
                   'Pintxos', 'Vino', 'Yoga', 'Meditación', 'Pilates', 'Spinning', 
                   'Crossfit', 'Gimnasio', 'Piscina', 'Paseo', 'Caminata', 
                   'Camping']