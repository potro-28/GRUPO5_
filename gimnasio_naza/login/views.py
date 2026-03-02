from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('gimnasio:listar_asistencia')
    
class logoutFormView(LogoutView):
    next_page = reverse_lazy('login:login')