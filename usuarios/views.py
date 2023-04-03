from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import random
from django.contrib.auth import get_user_model
from .forms import NewUserForm, UserProfileForm
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

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        user = authenticate(usuario, password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed!')
    else:
        return render(request, 'login.html', {})
    # login = AuthenticationForm()
    # return render(request, 'login.html', {'login_form':login})
 
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
