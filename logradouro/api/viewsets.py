from rest_framework.viewsets import ModelViewSet
from logradouro.models import Logradouro
from .serializers import LogradouroSerializer

class LogradouroViewSet(ModelViewSet):

    queryset = Logradouro.objects.all()
    serializer_class = LogradouroSerializer