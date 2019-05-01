from django.db import models
import datetime
# Create your models here.

class Gestor(models.Model):
    nome= models.CharField(max_length=400)
    email=models.CharField(max_length=400)
    username=models.CharField(max_length=400)
    password=models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    actived = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "gestores"
    
    def __str__(self):
        return self.nome
