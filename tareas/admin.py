from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridad', 'vigente', 'fecha_creacion', 'fecha_limite')
    list_filter = ('prioridad', 'vigente')
    search_fields = ('titulo', 'descripcion')

admin.site.register(Tarea, TareaAdmin)
