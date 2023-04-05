from django.db import models

class Jugador(models.Model):
    NUMERO_CHOICES = [
        ('1', 'Pilar izquierdo'),
        ('2', 'Hooker'),
        ('3', 'Pilar derecho'),
        ('4', 'Segunda línea'),
        ('5', 'Segunda línea'),
        ('6', 'Ala'),
        ('7', 'Ala'),
        ('8', 'Octavo'),
        ('9', 'Medio scrum'),
        ('10', 'Apertura'),
        ('11', 'Wing'),
        ('12', 'Centro'),
        ('13', 'Centro'),
        ('14', 'Wing'),
        ('15', 'Zaguero'),
    ]
    numero = models.CharField(max_length=2, choices=NUMERO_CHOICES)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tackles = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.numero} - {self.apellido}, {self.nombre}"


# Create your models here.
