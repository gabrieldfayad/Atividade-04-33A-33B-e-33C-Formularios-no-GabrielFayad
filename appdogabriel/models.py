from django.db import models

class Lanches(models.Model):
  titulo= models.CharField(max_length=50)
  localizacao= models.CharField(max_length=100)
  melhorLanche= models.CharField(max_length=100)
  nota= models.FloatField()

class Almocos(models.Model):
  titulo= models.CharField(max_length=50)
  localizacao= models.CharField(max_length=100)
  notaComida= models.FloatField()
  notaPreco= models.FloatField()

class Tabela(models.Model):
  restaurante= models.CharField(max_length=50)
  nota= models.FloatField()