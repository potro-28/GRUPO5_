from django.urls import path
from .views import DashboardUsuarioView, MiNutricionView,MiRutinaView,MiCertificacionView,MisSancionesView

app_name = 'usuarios'

urlpatterns = [
    path('dashboard/', DashboardUsuarioView.as_view(), name='dashboard_usuario'),
    path('mi-nutricion/', MiNutricionView.as_view(), name='mi_nutricion'),
    path('mi-rutina/',MiRutinaView.as_view(),name='mi_rutina'),
    path('mi-certificacion/',MiCertificacionView.as_view(),name='mi_certificacion'),
    path('mis-sanciones',MisSancionesView.as_view(),name='mi_sancion')
]