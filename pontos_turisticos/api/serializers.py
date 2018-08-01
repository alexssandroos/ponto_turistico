from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontoTuristico
from logradouro.api.serializers import LogradouroSerializer
from atracoes.api.serializers import AtracaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
	logradouro = LogradouroSerializer()
	atracao = AtracaoSerializer(many=True)

	class Meta:
		model = PontoTuristico
		fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
        	'logradouro', 'atracao')