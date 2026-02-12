from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from gimnasio.models import Usuario
from gimnasio.forms import usuarioForm


# =============================
# LISTAR USUARIOS
# =============================
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/listar.html'
    context_object_name = 'usuarios'
    ordering = ['-id']

    def get_queryset(self):
        return Usuario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Listado de Usuarios'
        context['crear_url'] = reverse_lazy('gimnasio:crear_usuario')

        return context


# =============================
# CREAR USUARIO
# =============================
class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = usuarioForm
    template_name = 'usuarios/crear.html'
    success_url = reverse_lazy('gimnasio:listar_usuarios')

    def form_valid(self, form):
        messages.success(self.request, "Usuario creado correctamente")
        return super().form_valid(form)


# =============================
# ACTUALIZAR USUARIO
# =============================

class UsuarioUpdateView(UpdateView):

    model = Usuario
    form_class = usuarioForm
    template_name = 'usuarios/editar.html'
    success_url = reverse_lazy('gimnasio:listar_usuarios')

    def form_valid(self, form):

        usuario = form.save(commit=False)

        # puedes hacer lógica extra aquí si deseas
        if usuario.activo:
            messages.success(self.request, "Usuario ACTIVADO correctamente")
        else:
            messages.warning(self.request, "Usuario INACTIVADO correctamente")

        usuario.save()

        return super().form_valid(form)


# =============================
# ELIMINAR USUARIO
# =============================
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_usuarios')
    context_object_name = 'usuario'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Usuario eliminado correctamente")
        return super().delete(request, *args, **kwargs)


# =============================
# ASIGNAR ROL A USUARIO
# =============================
class UsuarioRolUpdateView(UpdateView):
    model = Usuario
    form_class = usuarioForm
    template_name = 'usuarios/asignar_rol.html'
    success_url = reverse_lazy('gimnasio:listar_usuarios')

    def form_valid(self, form):
        messages.success(self.request, "Rol asignado correctamente")
        return super().form_valid(form)
