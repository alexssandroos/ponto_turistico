from django.db import models

# Create your models here.

class Logradouro(models.Model):
	logradouro = models.CharField(max_length=150)
	complemento = models.CharField(max_length=100)
	cidade = models.CharField(max_length=50)

	def __str__(self):
		return self.cidade + ' ' + self.logradouro