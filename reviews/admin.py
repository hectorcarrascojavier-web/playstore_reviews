from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AppReview

@admin.register(AppReview)
class AppReviewAdmin(admin.ModelAdmin):
    list_display = ('nombre_app', 'categoria', 'calificacion', 'descargas', 'fecha_registro')
    list_filter = ('categoria', 'calificacion')
    search_fields = ('nombre_app', 'reseña')
    list_editable = ('calificacion',)