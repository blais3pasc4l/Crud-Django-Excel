from django.db import models

# Create your models here.


class Modelos(models.Model):
    name_client = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    user_created = models.CharField(max_length=50)
    is_active = models.CharField(max_length=50)
    fechas_de_control = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
