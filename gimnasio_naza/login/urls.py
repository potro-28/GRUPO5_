from django.urls import path
from login.views import *

app_name = 'login'
urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', logoutFormView.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='registrarse'),
    path('password_reset/', PasswordResetView.as_view(), name='recuperar'),
    path('confirmar_correo/', ConfirmarCorreoView.as_view(), name='confirmar_correo'),
]