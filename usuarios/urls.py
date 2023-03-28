from django.urls import path
from usuarios import views
# from buscoAmigosApp.views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout'),
    path('registro/', views.pagina_registro, name='registro'),
    path('about/', views.about, name='about'),
]