from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import random
from django.contrib.auth import get_user_model
from .forms import UserForm, UserProfileForm

user = get_user_model()


# Create your views here.



def index(request):
    return render(request, 'home.html')

def signup(request):
    user_form = UserForm()
    return render(request, 'signup.html', {'user_form':user_form})

def pagina_registro(request):
    registrado = False
    user_form = UserForm() 
    user_profile = UserProfileForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_profile = UserProfileForm(data=request.POST)
        if form.is_valid() and user_profile.is_valid():
            form.save()
            # user_profile.save()
            user = form.save()
            # user.set_password(user.password)
            # user.save()
            
            profile = user_profile.save(commit=False)
            profile.user = user 
            registrado = True
        else:
            print('Error, Form is invalid')
        
        
    return render(request, 'signup.html', {'user_form':user_form,'user_profile':user_profile})
    # else:
    #     form = UserCreationForm() 

    # #     user_form = UserCreationForm()
    # #     user_profile = UserProfileForm()
    #     return render(request, 'signup.html', {'form':form})
    # #               {'user_form':form,
    # #               'user_profile':user_profile,
    # #               'registrado':registrado})


def about(request):
    return render(request, 'about.html')    


def login_page(request):
    login = AuthenticationForm()
    return render(request, 'login.html', {'login_form':login})

def logout_page(request):
    return render(request, 'logout.html')

# def custom_login(request):
#     if request.user.is_authenticated:
#         return redirect('homepage')

#     form = AuthenticationForm() 
    
#     return render(
#         request=request,
#         template_name="users/login.html", 
#         context={'form': form}
#         )

# def my_view(request):
#     email = request.POST['email']
#     password = request.POST['password']
#     user = authenticate(request, email=email, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...


# class LoginView(generic.CreateView):
#     form_class = User


# def rand_prof_pic(request):
#     rand_photo = (f'/templates/buscoAmigosApp/Images/{random.randint(1, 2031)}.jpg')
#     return render(request, 'home.html',{'rand_photo':rand_photo})