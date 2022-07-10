from django.shortcuts import render
from .models import Alumnos, Comentario, ComentarioContacto
from .forms import AlumnosForm, ComentarioContactoForm
from django.shortcuts import get_object_or_404

def registroAlumnos(request):
    alumno = Alumnos.objects.all()
    return render(request, 'registros/registroAlumnos.html', {'alumno': alumno})

def registrarAlumno(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
            alumnos = Alumnos.objects.all()
            return render(request, 'registros/principal.html', {'alumnos': alumnos})
        form = AlumnosForm()
        # Si algo sale mal se reenvia al formulario los datos ingresados
        return render(request, 'registros/registroAlumnos.html', {'form': form})

# Eliminar Alumno
def eliminarAlumno(request, id, confirmacion2 = 'registros/confirmarEliminacionAlumno.html'):
    alumno = get_object_or_404(Alumnos, id=id)
    if request.method == 'POST':
        alumno.delete()
        alumnos = Alumnos.objects.all()
        return render(request, 'registros/principal.html', {'alumnos': alumnos})
    return render(request, confirmacion2, {'object': alumno})

def consultarAlumno(request, id):
    alumno = Alumnos.objects.get(id=id)
    return render(request, 'registros/registroAlumnos.html', {'alumno': alumno})


# Eliminar//

# Editar
def editarAlumno(request, id):
    alumno = get_object_or_404(Alumnos, id=id)
    form = AlumnosForm(request.POST, instance=alumno)
    
    if form.is_valid():
            form.save()
            alumnos = Alumnos.objects.all()
            return render(request, 'registros/principal.html', {'alumnos': alumnos})
    return render(request, 'registros/formEditarAlumno.html', {'alumno':alumno})

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
    