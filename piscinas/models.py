from django.db import models

# Create your models here.
class Laguna(models.Model):
    estado = models.CharField(max_length=250, default="N/A")
    nombre = models.CharField(max_length=250, default="Sin nombre")
    nivelOD = models.FloatField(default=0)
    nivelORP = models.FloatField(default=0)
    estadoORP = models.CharField(max_length=250, default="N/A")
    estadoOD = models.CharField(max_length=250, default="N/A")

    def __str__(self):
        return self.nombre

class Aireador(models.Model):
    potencia = models.FloatField(default=0)
    consumoActual = models.FloatField(default=0)
    fechaUltimaPausa = models.DateField(auto_now=True)
    isOn = models.BooleanField(default=False)
    laguna = models.ForeignKey(Laguna, on_delete=models.CASCADE)

    def __str__(self):
        return (self.laguna.nombre + " - " + str(self.id))