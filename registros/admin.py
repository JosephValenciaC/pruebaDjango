from typing import Sequence
from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

class AdministarModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields: Sequence[str] = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')

admin.site.register(Alumnos, AdministarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields: Sequence[str] = ('id','created')
    date_hierarchy = 'created'
    readonly_fields: Sequence[str] = ('created', 'id')
    
admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id','usuario','mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields: Sequence[str] = ('created', 'id')
    
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)