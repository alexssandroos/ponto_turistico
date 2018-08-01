from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated


class PontoTuristicoViewSet(ModelViewSet):

	serializer_class = PontoTuristicoSerializer
	lookup_field = 'nome'
	permission_classes = (IsAuthenticated,)

# FIltros personalizados no queryset podem ser feitos com a subscricao 
# do metodo get_queryset, feito isso no core deve ser passado o parametro
# da classe base_name=NomeDaClasse

	def get_queryset(self):
		return PontoTuristico.objects.filter(aprovado=True)    