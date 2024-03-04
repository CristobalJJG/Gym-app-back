from django.contrib import admin
from .models import Entrenamiento, Ejercicio, Serie


# Register your models here.
class EjercicioInLine(admin.TabularInline):
    model = Ejercicio
    extra = 3


class SerieInLine(admin.TabularInline):
    model = Serie
    extra = 3


class EntrenamientoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['fecha']}),
        (None,               {'fields': ['duracion']}),
        (None,               {'fields': ['calorias']})
    ]
    inlines = [EjercicioInLine]
    list_display = ('fecha', 'duracion', 'calorias')


class EjercicioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        (None,               {'fields': ['entrenamiento_id']})
    ]
    inlines = [SerieInLine]
    list_display = ('nombre', 'entrenamiento_id')


class SerieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ejercicio_id']}),
        (None,               {'fields': ['repeticiones']}),
        (None,               {'fields': ['peso']})
    ]
    list_display = ('ejercicio_id', 'repeticiones', 'peso')


admin.site.register(Entrenamiento, EntrenamientoAdmin)
admin.site.register(Ejercicio, EjercicioAdmin)
admin.site.register(Serie, SerieAdmin)