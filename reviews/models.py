from django.db import models

class AppReview(models.Model):
    
    CATEGORIAS = [
        ('Juegos', 'Juegos'),
        ('Social', 'Social'),
        ('Productividad', 'Productividad'),
        ('Educación', 'Educación'),
        ('Entretenimiento', 'Entretenimiento'),
        ('Herramientas', 'Herramientas'),
        ('Fotografía', 'Fotografía'),
    ]
    
    nombre_app = models.CharField(max_length=200, verbose_name="Nombre de la app")
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, verbose_name="Categoría")
    calificacion = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Calificación (0-5)")
    descargas = models.CharField(max_length=50, verbose_name="Descargas aprox.")
    reseña = models.TextField(verbose_name="Reseña del usuario")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de registro")
    
    def __str__(self):
        return f"{self.nombre_app} - {self.calificacion} ⭐"
    
    class Meta:
        verbose_name = "Reseña de App"
        verbose_name_plural = "Reseñas de Apps"
        ordering = ['-calificacion']