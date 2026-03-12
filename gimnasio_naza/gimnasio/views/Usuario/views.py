from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from gimnasio.models import Usuario
from gimnasio.forms import UsuarioForm


# =============================
# LISTAR USUARIOS
# =============================
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/listar.html'
    context_object_name = 'object_list'  # Cambiado de 'usuarios' para que coincida con el template
    ordering = ['-id']

    def get_queryset(self):
        return Usuario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['crear_url'] = reverse_lazy('gimnasio:crear_usuario')  # Sin el '2'
        return context


# =============================
# CREAR USUARIO
# =============================
class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/crear.html'
    success_url = reverse_lazy('gimnasio:listar_usuario')
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Usuario'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Usuario creado correctamente")
        return super().form_valid(form)


# =============================
# ACTUALIZAR USUARIO
# =============================
class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/crear.html'  # Usa el mismo template que crear
    success_url = reverse_lazy('gimnasio:listar_usuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Usuario'
        return context

    def form_valid(self, form):
        usuario = form.save(commit=False)
        
        # Lógica extra si deseas
        if hasattr(usuario, 'activo'):
            if usuario.activo:
                messages.success(self.request, "Usuario ACTIVADO correctamente")
            else:
                messages.warning(self.request, "Usuario INACTIVADO correctamente")
        else:
            messages.success(self.request, "Usuario actualizado correctamente")
        
        usuario.save()
        return super().form_valid(form)


# =============================
# ELIMINAR USUARIO
# =============================
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar.html'
    success_url = reverse_lazy('gimnasio:listar_usuario')
    context_object_name = 'object'  # Cambiado para que coincida con el template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Usuario'
        context['listar_url'] = reverse_lazy('gimnasio:listar_usuario')
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Usuario eliminado correctamente")
        return super().delete(request, *args, **kwargs)


# =============================
# ASIGNAR ROL A USUARIO
# =============================
class UsuarioRolUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/asignar_rol.html'
    success_url = reverse_lazy('gimnasio:listar_usuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Asignar Rol'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Rol asignado correctamente")
        return super().form_valid(form)