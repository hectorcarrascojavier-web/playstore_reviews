from django.shortcuts import render
from .models import AppReview

def inicio(request):
    """Página principal del proyecto"""
    return render(request, 'reviews/inicio.html')

def lista_registros(request):
    """Página que muestra todas las reseñas guardadas"""
    registros = AppReview.objects.all()
    return render(request, 'reviews/lista_registros.html', {'registros': registros})