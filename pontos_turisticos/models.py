from django.db import models
from atracoes.models import Atracao
from logradouro.models import Logradouro
# Create your models here.

class PontoTuristico(models.Model):
	nome = models.CharField(max_length=150)
	descricao = models.TextField()
	aprovado = models.BooleanField(default=False)
	atracao = models.ManyToManyField(Atracao)
	logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome