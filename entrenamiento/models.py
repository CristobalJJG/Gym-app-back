from django.db import models

# Create your models here.
class Entrenamiento(models.Model):
    entrenamiento_id = models.AutoField(primary_key=True)
    fecha = models.TextField()
    duracion = models.TextField()
    calorias = models.IntegerField()
    def __str__(self):
        return self.fecha
    
class Ejercicio(models.Model):
    ejercicio_id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    entrenamiento_id = models.ForeignKey(Entrenamiento, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Serie(models.Model):
    serie_id = models.AutoField(primary_key=True)
    ejercicio_id = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    repeticiones = models.IntegerField()
    peso = models.IntegerField()
    def __str__(self):
        return str(self.serie_id)