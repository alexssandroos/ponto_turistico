from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from logradouro.models import Logradouro
from .serializers import LogradouroSerializer

class LogradouroViewSet(ModelViewSet):

    queryset = Logradouro.objects.all()
    serializer_class = LogradouroSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('logradouro', 'cidade')