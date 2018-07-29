from rest_framework.serializers import ModelSerializer
from logradouro.models import Logradouro

class LogradouroSerializer(ModelSerializer):
    class Meta:
        model = Logradouro
        fields = ('id', 'logradouro', 'complemento', 'cidade')