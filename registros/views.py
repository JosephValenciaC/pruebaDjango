from django.shortcuts import render
from .models import Alumnos, Comentario, ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404

# Eliminar Alumno
def eliminarAlumno(request, id, confirmacion2 = 'registros/confirmarEliminacionAlumno.html'):
    alumno = get_object_or_404(Alumnos, id=id)
    if request.method == 'POST':
        alumno.delete()
        alumnos = Alumnos.objects.all()
        return render(request, 'registros/principal.html', {'alumnos': alumnos})
    return render(request, confirmacion2, {'object': alumno})


def editarAlumno(request, id):
    alumno = get_object_or_404(Alumnos, id=id)


def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos':alumnos})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
        form = ComentarioContactoForm()
        # Si algo sale mal se reenvia al formulario los datos ingresados
        return render(request, 'registros/contacto.html', {'form': form})
    
    # Eliminar Comentario
def eliminarComentarioContacto(request, id, 
    confirmacion = 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

def consultarComentario(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, 'registros/formEditarComentario.html', {'comentario': comentario})
# Eliminar//



# Editar
def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, 'registros/formEditarComentario.html', {'comentario':comentario })

# /Editar


def contacto(request):
    return render(request, "registros/contacto.html")


def coment(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    